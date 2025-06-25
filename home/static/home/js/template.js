document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const navbarToggle = document.getElementById('navbarToggle');
    const navbar = document.querySelector('.navbar-template');
    
    if (navbarToggle) {
        navbarToggle.addEventListener('click', function() {
            navbar.classList.toggle('active');
            // Change icon based on menu state
            const icon = this.querySelector('i');
            if (navbar.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }
    
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!event.target.closest('.navbar-template') && 
            !event.target.closest('.navbar-mobile-toggle-template') && 
            navbar && navbar.classList.contains('active')) {
            navbar.classList.remove('active');
            if (navbarToggle) {
                const icon = navbarToggle.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        }
    });
    
    // User dropdown toggle
    window.toggleDropdown = function() {
        const dropdown = document.getElementById('profileDropdown');
        dropdown.classList.toggle('show');
        
        // Close dropdown when clicking outside
        document.addEventListener('click', function closeDropdown(event) {
            if (!event.target.matches('.user-icon-template') && 
                !event.target.closest('.dropdown-content-template')) {
                dropdown.classList.remove('show');
                document.removeEventListener('click', closeDropdown);
            }
        });
    };
    
    // Search form toggle
    const searchToggle = document.getElementById('searchToggle');
    const searchForm = document.getElementById('searchForm');
    
    if (searchToggle && searchForm) {
        searchToggle.addEventListener('click', function() {
            searchForm.classList.toggle('show');
            
            // Focus on input when search form is shown
            if (searchForm.classList.contains('show')) {
                searchForm.querySelector('.search-input-template').focus();
            }
            
            // Close search form when clicking outside
            document.addEventListener('click', function closeSearch(event) {
                if (!event.target.closest('.search-template')) {
                    searchForm.classList.remove('show');
                    document.removeEventListener('click', closeSearch);
                }
            });
        });
    }
    
    // Add active class to current page link
    const currentLocation = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link-template');
    
    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (linkPath === currentLocation || 
            (linkPath !== '/' && currentLocation.startsWith(linkPath))) {
            link.classList.add('active');
        }
    });
});