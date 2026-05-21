// Dark Mode Toggle
const toggleButton = document.getElementById('theme-toggle');

if (toggleButton) {
    function getStoredTheme() {
        try {
            return localStorage.getItem('arxiv-daily-theme');
        } catch (error) {
            return null;
        }
    }

    function setStoredTheme(theme) {
        try {
            localStorage.setItem('arxiv-daily-theme', theme);
        } catch (error) {
            // Theme persistence is optional; keep the toggle usable without storage.
        }
    }

    function updateThemeToggle() {
        const isDark = document.body.classList.contains('dark-mode');
        toggleButton.textContent = isDark ? '☀️ Day' : '🌙 Night';
        toggleButton.setAttribute('aria-label', isDark ? 'Switch to light theme' : 'Switch to dark theme');
    }

    if (getStoredTheme() === 'dark') {
        document.body.classList.add('dark-mode');
    }

    updateThemeToggle();

    toggleButton.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        setStoredTheme(document.body.classList.contains('dark-mode') ? 'dark' : 'light');
        updateThemeToggle();
    });
}
