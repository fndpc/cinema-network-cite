document.addEventListener('DOMContentLoaded', function() {
    const userIcon = document.querySelector('.fa-regular.fa-user');
    const dropdown = document.getElementById('profileDropdown');

    function toggleDropdown() {
        dropdown.classList.toggle('show');
    }

    if (userIcon) {
        userIcon.addEventListener('click', function(event) {
            event.stopPropagation();
            toggleDropdown();
        });
    }

    // Закрыть при клике вне меню
    document.addEventListener('click', function(event) {
        if (!event.target.closest('.dropdown') && !event.target.closest('.dropdown-content')) {
            dropdown.classList.remove('show');
        }
    });
});