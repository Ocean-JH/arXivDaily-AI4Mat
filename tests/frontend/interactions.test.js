'use strict';

const assert = require('assert').strict;
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const repositoryRoot = path.resolve(__dirname, '..', '..');
const tests = [];

function test(name, callback) {
    tests.push({ name, callback });
}

function script(name) {
    return fs.readFileSync(path.join(repositoryRoot, 'static', 'js', name), 'utf8');
}

function paper(index, text) {
    return `<article class="paper" id="paper-${index}" tabindex="-1">
        <h3>${text}</h3>
        <p>Author ${index}</p>
        <details><summary>Abstract</summary><p>Summary ${index}</p></details>
    </article>`;
}

function pageMarkup(options = {}) {
    const papers = options.papers || '';
    const pageType = options.pageType || 'latest';
    const archiveIndex = options.archiveIndex || '';

    return `<!doctype html>
        <html><body data-page-type="${pageType}" data-archive-search-index="${archiveIndex}">
            <main>
                <form id="paper-search"><input id="search-input"><button type="submit">Search</button></form>
                <p id="search-results-info" hidden></p>
                <section id="archive-search-results" hidden>
                    <p id="archive-search-summary"></p>
                    <ol id="archive-search-list"></ol>
                </section>
                <div id="papers-content">${papers}</div>
            </main>
        </body></html>`;
}

function makeDom(markup, url = 'https://example.test/index.html') {
    const dom = new JSDOM(markup, {
        runScripts: 'outside-only',
        url
    });

    dom.window.matchMedia = () => ({
        matches: true,
        addEventListener() {}
    });
    dom.window.requestAnimationFrame = callback => callback();
    dom.window.HTMLElement.prototype.scrollIntoView = function () {};

    return dom;
}

test('latest pagination hides cards without overriding their display layout', () => {
    const papers = Array.from({ length: 12 }, (_, index) => paper(index + 1, `Paper ${index + 1}`)).join('');
    const dom = makeDom(pageMarkup({ papers }));

    dom.window.eval(script('pagination.js'));

    const cards = Array.from(dom.window.document.querySelectorAll('.paper'));
    const next = dom.window.document.querySelector('.pagination-button:last-child');

    assert.equal(cards.filter(card => !card.hidden).length, 10);
    assert.equal(cards.some(card => card.hasAttribute('style')), false);

    next.click();

    assert.equal(cards.filter(card => !card.hidden).length, 2);
    assert.equal(dom.window.document.activeElement, cards[10]);
    assert.match(dom.window.location.search, /page=2/);
});

test('latest search records the query, reports an exact count, and cooperates with pagination', () => {
    const papers = [
        paper(1, 'Graph neural networks for crystals'),
        paper(2, 'Diffusion for molecule generation'),
        paper(3, 'Graph learning for alloys')
    ].join('');
    const dom = makeDom(pageMarkup({ papers }));

    dom.window.eval(script('pagination.js'));
    dom.window.eval(script('search.js'));

    const input = dom.window.document.getElementById('search-input');
    input.value = 'graph';
    dom.window.document.getElementById('paper-search')
        .dispatchEvent(new dom.window.Event('submit', { bubbles: true, cancelable: true }));

    const cards = Array.from(dom.window.document.querySelectorAll('.paper'));
    assert.equal(cards.filter(card => !card.hidden).length, 2);
    assert.equal(cards.some(card => card.hasAttribute('style')), false);
    assert.equal(dom.window.document.getElementById('search-results-info').textContent,
        '2 papers found for “graph”.');
    assert.equal(new dom.window.URL(dom.window.location.href).searchParams.get('q'), 'graph');
});

test('archive search loads its index lazily and links to the owning static page', async () => {
    const dom = makeDom(pageMarkup({
        pageType: 'archive',
        archiveIndex: 'data/archive-search-index.json',
        papers: paper(1, 'Current page paper')
    }), 'https://example.test/archive.html');
    let fetchCount = 0;

    dom.window.fetch = async url => {
        fetchCount += 1;
        assert.equal(url, 'data/archive-search-index.json');
        return {
            ok: true,
            async json() {
                return {
                    papers: [{
                        id: '2601.00001v1',
                        base_id: '2601.00001',
                        title: 'Graph models for solid electrolytes',
                        authors: ['Ada Researcher'],
                        categories: ['cond-mat.mtrl-sci'],
                        primary_category: 'cond-mat.mtrl-sci',
                        summary: 'Graph learning for ionic transport.',
                        published: '2026-01-02T00:00:00+00:00',
                        page: 2,
                        anchor: 'paper-2601.00001'
                    }]
                };
            }
        };
    };

    dom.window.eval(script('search.js'));
    assert.equal(fetchCount, 0);

    const input = dom.window.document.getElementById('search-input');
    input.value = 'electrolytes';
    dom.window.document.getElementById('paper-search')
        .dispatchEvent(new dom.window.Event('submit', { bubbles: true, cancelable: true }));
    await new Promise(resolve => setImmediate(resolve));

    const link = dom.window.document.querySelector('.archive-search-item a');
    assert.equal(fetchCount, 1);
    assert.equal(dom.window.document.getElementById('papers-content').hidden, true);
    assert.equal(dom.window.document.getElementById('archive-search-results').hidden, false);
    assert.equal(link.getAttribute('href'), 'archive-2.html#paper-2601.00001');
});

test('theme initialization follows the system before the toggle stores an explicit choice', () => {
    const dom = makeDom(`<!doctype html><html data-theme="light"><head>
        <meta name="theme-color" content="#f4f1ea">
    </head><body>
        <button id="theme-toggle" aria-pressed="false">
            <span aria-hidden="true">◐</span><span class="theme-toggle-label">Theme</span>
        </button>
    </body></html>`);

    dom.window.eval(script('theme-init.js'));
    assert.equal(dom.window.document.documentElement.dataset.theme, 'dark');

    dom.window.eval(script('dark-mode.js'));
    dom.window.document.getElementById('theme-toggle').click();

    assert.equal(dom.window.document.documentElement.dataset.theme, 'light');
    assert.equal(dom.window.localStorage.getItem('arxiv-daily-theme'), 'light');
    assert.equal(dom.window.document.getElementById('theme-toggle').getAttribute('aria-pressed'), 'false');
});

(async function run() {
    for (const entry of tests) {
        await entry.callback();
        process.stdout.write(`✓ ${entry.name}\n`);
    }
}()).catch(error => {
    process.stderr.write(`${error.stack || error}\n`);
    process.exitCode = 1;
});
