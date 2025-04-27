
    const toggle = document.getElementById('theme-toggle');
    const body = document.body;

    // Проверяем сохраненную тему в localStorage
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme) {
        body.classList.toggle('light-theme', currentTheme === 'light');
        toggle.checked = currentTheme === 'light';
    }

    toggle.addEventListener('change', () => {
        body.classList.toggle('light-theme', toggle.checked);
        // Сохраняем выбранную тему в localStorage
        localStorage.setItem('theme', toggle.checked ? 'light' : 'dark');
    });

