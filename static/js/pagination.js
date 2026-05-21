// Pagination functionality for paper list
(function () {
    const papersPerPage = 10;
    const allPapers = Array.from(document.querySelectorAll('.paper'));

    if (allPapers.length === 0) {
        return;
    }

    let filteredPapers = allPapers;
    let currentPage = 1;

    const controls = document.createElement('div');
    controls.className = 'pagination-controls';
    controls.innerHTML = `
        <button id="pagination-prev" class="pagination-button" type="button">← Previous</button>
        <span id="pagination-info" class="pagination-info"></span>
        <button id="pagination-next" class="pagination-button" type="button">Next →</button>
    `;

    const lastPaper = allPapers[allPapers.length - 1];
    lastPaper.after(controls);

    const prevButton = document.getElementById('pagination-prev');
    const nextButton = document.getElementById('pagination-next');
    const pageInfo = document.getElementById('pagination-info');

    function render() {
        const totalPages = Math.max(1, Math.ceil(filteredPapers.length / papersPerPage));
        currentPage = Math.min(Math.max(currentPage, 1), totalPages);

        allPapers.forEach(paper => {
            paper.style.display = 'none';
        });

        const start = (currentPage - 1) * papersPerPage;
        const end = start + papersPerPage;
        filteredPapers.slice(start, end).forEach(paper => {
            paper.style.display = 'block';
        });

        pageInfo.textContent = `Page ${currentPage} of ${totalPages}`;
        prevButton.disabled = currentPage === 1;
        nextButton.disabled = currentPage === totalPages;

        controls.style.display = filteredPapers.length > papersPerPage ? 'flex' : 'none';
    }

    prevButton.addEventListener('click', function () {
        currentPage -= 1;
        render();
        controls.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });

    nextButton.addEventListener('click', function () {
        currentPage += 1;
        render();
        controls.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });

    window.paperPagination = {
        update(papers) {
            filteredPapers = papers;
            currentPage = 1;
            render();
        }
    };

    render();
})();
