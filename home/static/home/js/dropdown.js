let dropdownTimeout;

function toggleDropdown() {
    const dropdown = document.getElementById("profileDropdown");
    dropdown.classList.toggle("show");
    clearTimeout(dropdownTimeout); // Очищаем таймер, если меню открывается
}

function hideDropdown() {
    const dropdown = document.getElementById("profileDropdown");
    dropdownTimeout = setTimeout(() => {
        if (dropdown.classList.contains('show')) {
            dropdown.classList.remove("show");
        }
    }, 500); // Задержка перед скрытием (300 мс)
}

// Закрыть выпадающее меню, если кликнули вне его
window.onclick = function(event) {
    if (!event.target.matches('.fa-regular.fa-user') && !event.target.closest('.dropdown-content')) {
        hideDropdown();
    }
}

// Добавляем обработчики событий для наведения
const userIcon = document.querySelector('.fa-regular.fa-user');
userIcon.addEventListener('mouseenter', () => {
    clearTimeout(dropdownTimeout); // Очищаем таймер, если курсор на иконке
    toggleDropdown(); // Открываем меню при наведении на иконку
});

userIcon.addEventListener('mouseleave', hideDropdown);
document.getElementById("profileDropdown").addEventListener('mouseenter', () => {
    clearTimeout(dropdownTimeout); // Очищаем таймер, если курсор на меню
});
document.getElementById("profileDropdown").addEventListener('mouseleave', hideDropdown);
