(function () {
    'use strict';

    var storageKey = 'arxiv-daily-theme';
    var storedTheme = null;

    try {
        storedTheme = window.localStorage.getItem(storageKey);
    } catch (error) {
        // Storage is optional. The operating-system preference remains available.
    }

    var prefersDark = window.matchMedia
        && window.matchMedia('(prefers-color-scheme: dark)').matches;
    var theme = storedTheme === 'dark' || storedTheme === 'light'
        ? storedTheme
        : (prefersDark ? 'dark' : 'light');

    document.documentElement.dataset.theme = theme;
    document.documentElement.style.colorScheme = theme;

    var themeColor = document.querySelector('meta[name="theme-color"]');
    if (themeColor) {
        themeColor.setAttribute('content', theme === 'dark' ? '#111416' : '#f4f1ea');
    }
}());
