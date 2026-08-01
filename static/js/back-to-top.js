(function () {
    'use strict';

    var button = document.getElementById('back-to-top');
    var reduceMotion = window.matchMedia
        && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (!button) {
        return;
    }

    function updateVisibility() {
        button.hidden = window.scrollY <= 500;
    }

    window.addEventListener('scroll', updateVisibility, { passive: true });
    button.addEventListener('click', function () {
        window.scrollTo({
            top: 0,
            behavior: reduceMotion ? 'auto' : 'smooth'
        });
    });

    updateVisibility();
}());
