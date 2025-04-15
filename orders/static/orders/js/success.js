// Открытие модального окна
window.onload = function() {
    document.getElementById('successModal').style.display = 'block';
};

// Закрытие модального окна
document.getElementById('closeModal').onclick = function() {
    document.getElementById('successModal').style.display = 'none';
};

// Закрытие модального окна при клике вне его
window.onclick = function(event) {
    const modal = document.getElementById('successModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
};