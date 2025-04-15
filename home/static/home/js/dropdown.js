// static/home/js/dropdown.js
function toggleDropdown() {
    document.getElementById("profileDropdown").classList.toggle("show");
}

// Закрыть выпадающее меню, если кликнули вне его
window.onclick = function(event) {
    if (!event.target.matches('.fa-regular.fa-user')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}
