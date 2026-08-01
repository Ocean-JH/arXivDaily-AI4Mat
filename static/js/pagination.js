(function () {
    'use strict';

    var papersPerPage = 10;
    var body = document.body;
    var allPapers = Array.prototype.slice.call(document.querySelectorAll('.paper'));

    if (!body || body.dataset.pageType !== 'latest' || allPapers.length === 0) {
        return;
    }

    var filteredPapers = allPapers.slice();
    var currentPage = readPageFromUrl();
    var reduceMotion = window.matchMedia
        && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    var controls = document.createElement('nav');
    controls.className = 'pagination-controls';
    controls.setAttribute('aria-label', 'Latest paper pages');

    var previousButton = document.createElement('button');
    previousButton.className = 'pagination-button';
    previousButton.type = 'button';
    previousButton.textContent = '← Previous';

    var pageStatus = document.createElement('span');
    pageStatus.className = 'pagination-info';
    pageStatus.setAttribute('role', 'status');
    pageStatus.setAttribute('aria-live', 'polite');
    pageStatus.setAttribute('aria-atomic', 'true');

    var nextButton = document.createElement('button');
    nextButton.className = 'pagination-button';
    nextButton.type = 'button';
    nextButton.textContent = 'Next →';

    controls.append(previousButton, pageStatus, nextButton);
    allPapers[allPapers.length - 1].after(controls);

    function readPageFromUrl() {
        var page = Number.parseInt(new URL(window.location.href).searchParams.get('page'), 10);
        return Number.isFinite(page) && page > 0 ? page : 1;
    }

    function writePageToUrl(page, method) {
        var url = new URL(window.location.href);

        if (page > 1) {
            url.searchParams.set('page', String(page));
        } else {
            url.searchParams.delete('page');
        }

        window.history[method](null, '', url);
    }

    function focusFirstVisiblePaper(firstPaper) {
        if (!firstPaper) {
            return;
        }

        var focusAndScroll = function () {
            firstPaper.focus({ preventScroll: true });
            firstPaper.scrollIntoView({
                behavior: reduceMotion ? 'auto' : 'smooth',
                block: 'start'
            });
        };

        if (typeof window.requestAnimationFrame === 'function') {
            window.requestAnimationFrame(focusAndScroll);
        } else {
            focusAndScroll();
        }
    }

    function render(options) {
        var settings = options || {};
        var totalResults = filteredPapers.length;
        var totalPages = Math.max(1, Math.ceil(totalResults / papersPerPage));

        currentPage = Math.min(Math.max(currentPage, 1), totalPages);
        allPapers.forEach(function (paper) {
            paper.hidden = true;
        });

        var start = (currentPage - 1) * papersPerPage;
        var visiblePapers = filteredPapers.slice(start, start + papersPerPage);
        visiblePapers.forEach(function (paper) {
            paper.hidden = false;
        });

        if (totalResults === 0) {
            pageStatus.textContent = 'No matching papers';
        } else {
            var firstResult = start + 1;
            var lastResult = Math.min(start + papersPerPage, totalResults);
            pageStatus.textContent = 'Page ' + currentPage + ' of ' + totalPages
                + ' · papers ' + firstResult + '–' + lastResult + ' of ' + totalResults;
        }

        previousButton.disabled = currentPage === 1;
        nextButton.disabled = currentPage === totalPages;
        controls.hidden = totalResults <= papersPerPage;

        if (settings.updateUrl) {
            writePageToUrl(currentPage, settings.historyMethod || 'replaceState');
        }

        if (settings.focusResults) {
            focusFirstVisiblePaper(visiblePapers[0]);
        }
    }

    function movePage(offset) {
        currentPage += offset;
        render({
            updateUrl: true,
            historyMethod: 'pushState',
            focusResults: true
        });
    }

    previousButton.addEventListener('click', function () {
        movePage(-1);
    });

    nextButton.addEventListener('click', function () {
        movePage(1);
    });

    window.addEventListener('popstate', function () {
        currentPage = readPageFromUrl();
        render();
    });

    window.paperPagination = Object.freeze({
        update: function (papers, options) {
            var settings = options || {};
            filteredPapers = Array.isArray(papers) ? papers.slice() : [];
            currentPage = settings.page || 1;
            render({
                updateUrl: settings.updateUrl !== false,
                historyMethod: settings.historyMethod || 'replaceState',
                focusResults: Boolean(settings.focusResults)
            });
        },
        getPage: function () {
            return currentPage;
        }
    });

    render({ updateUrl: true });
}());
