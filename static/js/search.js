// Search functionality for a paper repository
const searchInput = document.getElementById('search-input');
const searchButton = document.getElementById('search-button');
const papers = Array.from(document.querySelectorAll('.paper'));

function updateVisiblePapers(visiblePapers) {
    if (window.paperPagination && typeof window.paperPagination.update === 'function') {
        window.paperPagination.update(visiblePapers);
        return;
    }

    if (visiblePapers === papers) {
        papers.forEach(paper => {
            paper.style.display = 'block';
        });
        return;
    }

    const visiblePaperSet = new Set(visiblePapers);
    papers.forEach(paper => {
        paper.style.display = visiblePaperSet.has(paper) ? 'block' : 'none';
    });
}

function performSearch() {
    const searchTerm = searchInput.value.trim().toLowerCase();
    const matchingPapers = papers.filter(paper => {
        const title = paper.querySelector('h3').textContent.toLowerCase();
        const authors = paper.querySelector('.paper-info').textContent.toLowerCase();
        const summary = paper.querySelector('details').textContent.toLowerCase();

        return title.includes(searchTerm) || authors.includes(searchTerm) || summary.includes(searchTerm);
    });

    const visiblePapers = searchTerm === '' ? papers : matchingPapers;
    updateVisiblePapers(visiblePapers);
    const resultsFound = matchingPapers.length > 0;

    // Display search results info
    const resultsInfo = document.getElementById('search-results-info');
    if (resultsInfo) {
        if (searchTerm === '') {
            resultsInfo.style.display = 'none';
        } else {
            resultsInfo.style.display = 'block';
            resultsInfo.textContent = resultsFound ?
                `Showing papers containing "${searchTerm}"` :
                `No papers were found containing "${searchTerm}"`;
        }
    } else {
        const infoElement = document.createElement('div');
        infoElement.id = 'search-results-info';
        infoElement.className = 'search-results-info';
        if (searchTerm !== '') {
            infoElement.textContent = resultsFound ?
                `Showing papers containing "${searchTerm}"` :
                `No papers were found containing "${searchTerm}"`;
        } else {
            infoElement.style.display = 'none';
        }
        document.querySelector('.search-container').after(infoElement);
    }
}

if (searchButton && searchInput) {
    searchButton.addEventListener('click', performSearch);
    searchInput.addEventListener('keyup', function (event) {
        if (event.key === 'Enter') {
            performSearch();
        }
    });
}
