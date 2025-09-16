// Written entirely by Gemini because I hate Javascript.
// P.S. How do people vibe code? I've run this code through three AIs and
// still can't fix an issue
document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;
    const themeIcon = document.getElementById('theme-icon');

    const getPreferredTheme = () => {
        const storedTheme = localStorage.getItem('theme');
        if (storedTheme) {
            return storedTheme;
        }
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    };

    const setTheme = (theme) => {
        htmlElement.setAttribute('data-bs-theme', theme);
        localStorage.setItem('theme', theme);

        // Update the icon's data attribute based on the new theme
        if (theme === 'dark') {
            themeIcon.setAttribute('data-lucide', 'sun');
        } else {
            themeIcon.setAttribute('data-lucide', 'moon');
        }

        // Re-create icons
        // TODO: Currently, this DOESN'T WORK!
        //  The icon is only changed upon a page refresh. THIS NEEDS TO BE FIXED!
        lucide.createIcons();
    };

    // Set initial theme and icon on page load
    setTheme(getPreferredTheme());

    // Add event listener to toggle button
    themeToggle.addEventListener('click', () => {
        const currentTheme = htmlElement.getAttribute('data-bs-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
    });
});