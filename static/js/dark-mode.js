(function () {
    'use strict';

    var root = document.documentElement;
    var toggle = document.getElementById('theme-toggle');
    var storageKey = 'arxiv-daily-theme';
    var mediaQuery = window.matchMedia
        ? window.matchMedia('(prefers-color-scheme: dark)')
        : null;

    if (!toggle) {
        return;
    }

    function getStoredTheme() {
        try {
            var value = window.localStorage.getItem(storageKey);
            return value === 'dark' || value === 'light' ? value : null;
        } catch (error) {
            return null;
        }
    }

    function storeTheme(theme) {
        try {
            window.localStorage.setItem(storageKey, theme);
        } catch (error) {
            // Theme persistence is an enhancement; the toggle still works.
        }
    }

    function applyTheme(theme) {
        var isDark = theme === 'dark';
        var icon = toggle.querySelector('[aria-hidden="true"]');
        var label = toggle.querySelector('.theme-toggle-label');
        var themeColor = document.querySelector('meta[name="theme-color"]');

        root.dataset.theme = isDark ? 'dark' : 'light';
        root.style.colorScheme = isDark ? 'dark' : 'light';
        toggle.setAttribute('aria-pressed', String(isDark));
        toggle.setAttribute('aria-label', isDark ? 'Switch to light theme' : 'Switch to dark theme');

        if (icon) {
            icon.textContent = isDark ? '☀' : '☾';
        }

        if (label) {
            label.textContent = isDark ? 'Light' : 'Dark';
        }

        if (themeColor) {
            themeColor.setAttribute('content', isDark ? '#111416' : '#f4f1ea');
        }
    }

    toggle.addEventListener('click', function () {
        var nextTheme = root.dataset.theme === 'dark' ? 'light' : 'dark';
        applyTheme(nextTheme);
        storeTheme(nextTheme);
    });

    if (mediaQuery) {
        var handleSystemThemeChange = function (event) {
            if (!getStoredTheme()) {
                applyTheme(event.matches ? 'dark' : 'light');
            }
        };

        if (typeof mediaQuery.addEventListener === 'function') {
            mediaQuery.addEventListener('change', handleSystemThemeChange);
        } else if (typeof mediaQuery.addListener === 'function') {
            mediaQuery.addListener(handleSystemThemeChange);
        }
    }

    applyTheme(root.dataset.theme === 'dark' ? 'dark' : 'light');
}());
