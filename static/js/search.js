(function () {
    'use strict';

    var resultLimit = 100;
    var body = document.body;
    var form = document.getElementById('paper-search');
    var input = document.getElementById('search-input');
    var status = document.getElementById('search-results-info');
    var papersContent = document.getElementById('papers-content');
    var archiveResults = document.getElementById('archive-search-results');
    var archiveSummary = document.getElementById('archive-search-summary');
    var archiveList = document.getElementById('archive-search-list');

    if (!body || !form || !input || !status || !papersContent) {
        return;
    }

    var pageType = body.dataset.pageType;
    var localPapers = Array.prototype.slice.call(document.querySelectorAll('.paper'));
    var archiveIndexPromise = null;
    var searchSequence = 0;

    function normalized(value) {
        return String(value || '').trim().toLocaleLowerCase();
    }

    function queryFromUrl() {
        return new URL(window.location.href).searchParams.get('q') || '';
    }

    function pageFromUrl() {
        var page = Number.parseInt(new URL(window.location.href).searchParams.get('page'), 10);
        return Number.isFinite(page) && page > 0 ? page : 1;
    }

    function writeQueryToUrl(query, method) {
        var url = new URL(window.location.href);

        if (query) {
            url.searchParams.set('q', query);
        } else {
            url.searchParams.delete('q');
        }

        url.searchParams.delete('page');
        window.history[method](null, '', url);
    }

    function setStatus(message) {
        status.textContent = message;
        status.hidden = !message;
    }

    function matchesQuery(searchableText, query) {
        var words = normalized(query).split(/\s+/).filter(Boolean);
        var text = normalized(searchableText);
        return words.every(function (word) {
            return text.includes(word);
        });
    }

    function searchLatest(query, options) {
        var settings = options || {};
        var trimmedQuery = query.trim();
        var matchingPapers = trimmedQuery
            ? localPapers.filter(function (paper) {
                return matchesQuery(paper.textContent, trimmedQuery);
            })
            : localPapers;

        if (window.paperPagination && typeof window.paperPagination.update === 'function') {
            window.paperPagination.update(matchingPapers, {
                page: settings.page || 1,
                updateUrl: false,
                focusResults: false
            });
        } else {
            var matchingSet = new Set(matchingPapers);
            localPapers.forEach(function (paper) {
                paper.hidden = !matchingSet.has(paper);
            });
        }

        if (!trimmedQuery) {
            setStatus('');
            return;
        }

        var noun = matchingPapers.length === 1 ? 'paper' : 'papers';
        setStatus(matchingPapers.length + ' ' + noun + ' found for “' + trimmedQuery + '”.');
    }

    function loadArchiveIndex() {
        if (archiveIndexPromise) {
            return archiveIndexPromise;
        }

        var indexUrl = body.dataset.archiveSearchIndex;
        if (!indexUrl || typeof window.fetch !== 'function') {
            return Promise.reject(new Error('Archive search is unavailable.'));
        }

        archiveIndexPromise = window.fetch(indexUrl, {
            headers: { Accept: 'application/json' }
        }).then(function (response) {
            if (!response.ok) {
                throw new Error('Archive index returned ' + response.status + '.');
            }
            return response.json();
        }).then(function (data) {
            if (!data || !Array.isArray(data.papers)) {
                throw new Error('Archive index has an unexpected format.');
            }
            return data.papers;
        }).catch(function (error) {
            archiveIndexPromise = null;
            throw error;
        });

        return archiveIndexPromise;
    }

    function archivePaperText(paper) {
        return [
            paper.id,
            paper.base_id,
            paper.title,
            Array.isArray(paper.authors) ? paper.authors.join(' ') : paper.authors,
            Array.isArray(paper.categories) ? paper.categories.join(' ') : paper.categories,
            paper.primary_category,
            paper.summary
        ].join(' ');
    }

    function safeAnchor(paper) {
        var candidate = String(paper.anchor || '');
        if (/^[A-Za-z][A-Za-z0-9_:.-]*$/.test(candidate)) {
            return candidate;
        }

        return 'paper-' + String(paper.base_id || paper.id || '')
            .replace(/[^A-Za-z0-9_.-]+/g, '-');
    }

    function archivePageHref(paper) {
        var page = Number.parseInt(paper.page, 10);
        var fileName = Number.isFinite(page) && page > 1
            ? 'archive-' + page + '.html'
            : 'archive.html';
        return fileName + '#' + encodeURIComponent(safeAnchor(paper));
    }

    function renderArchiveResults(matches, query) {
        var shownPapers = matches.slice(0, resultLimit);
        var fragment = document.createDocumentFragment();

        archiveList.replaceChildren();

        shownPapers.forEach(function (paper) {
            var item = document.createElement('li');
            var link = document.createElement('a');
            var meta = document.createElement('p');
            var metaParts = [];

            item.className = 'archive-search-item';
            link.href = archivePageHref(paper);
            link.textContent = paper.title || paper.id || 'Untitled paper';

            if (paper.id || paper.base_id) {
                metaParts.push(paper.id || paper.base_id);
            }
            if (paper.primary_category) {
                metaParts.push(paper.primary_category);
            }
            if (paper.published) {
                metaParts.push(String(paper.published).slice(0, 10));
            }
            if (Array.isArray(paper.authors) && paper.authors.length > 0) {
                var authorText = paper.authors.slice(0, 3).join(', ');
                if (paper.authors.length > 3) {
                    authorText += ' et al.';
                }
                metaParts.push(authorText);
            }

            meta.className = 'archive-search-meta';
            meta.textContent = metaParts.join(' · ');
            item.append(link, meta);
            fragment.append(item);
        });

        if (shownPapers.length === 0) {
            var emptyItem = document.createElement('li');
            emptyItem.className = 'archive-search-empty';
            emptyItem.textContent = 'No archive papers matched “' + query + '”.';
            fragment.append(emptyItem);
        }

        archiveList.append(fragment);
        papersContent.hidden = true;
        archiveResults.hidden = false;

        var noun = matches.length === 1 ? 'paper' : 'papers';
        var summary = matches.length + ' ' + noun + ' found for “' + query + '”.';
        if (matches.length > resultLimit) {
            summary += ' Showing the first ' + resultLimit + '.';
        }
        archiveSummary.textContent = summary;
        setStatus(summary);
    }

    function clearArchiveSearch() {
        searchSequence += 1;
        papersContent.hidden = false;
        archiveResults.hidden = true;
        archiveList.replaceChildren();
        archiveSummary.textContent = '';
        setStatus('');
    }

    function searchArchive(query) {
        var trimmedQuery = query.trim();
        var sequence = ++searchSequence;

        if (!trimmedQuery) {
            clearArchiveSearch();
            return;
        }

        setStatus('Searching the complete archive…');

        loadArchiveIndex().then(function (papers) {
            if (sequence !== searchSequence) {
                return;
            }

            var matches = papers.filter(function (paper) {
                return matchesQuery(archivePaperText(paper), trimmedQuery);
            });
            renderArchiveResults(matches, trimmedQuery);
        }).catch(function () {
            if (sequence !== searchSequence) {
                return;
            }

            papersContent.hidden = false;
            archiveResults.hidden = true;
            setStatus('The complete archive search could not be loaded. You can still browse this page.');
        });
    }

    function runSearch(query, options) {
        var settings = options || {};
        input.value = query;

        if (settings.updateUrl) {
            writeQueryToUrl(query.trim(), settings.historyMethod || 'pushState');
        }

        if (pageType === 'archive') {
            searchArchive(query);
        } else {
            searchLatest(query, { page: settings.page || 1 });
        }
    }

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        runSearch(input.value, {
            updateUrl: true,
            historyMethod: 'pushState',
            page: 1
        });
    });

    input.addEventListener('search', function () {
        if (!input.value) {
            runSearch('', {
                updateUrl: true,
                historyMethod: 'pushState',
                page: 1
            });
        }
    });

    window.addEventListener('popstate', function () {
        runSearch(queryFromUrl(), {
            updateUrl: false,
            page: pageFromUrl()
        });
    });

    var initialQuery = queryFromUrl();
    if (initialQuery) {
        runSearch(initialQuery, {
            updateUrl: false,
            page: pageFromUrl()
        });
    }
}());
