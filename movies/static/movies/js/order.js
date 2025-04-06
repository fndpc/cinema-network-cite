document.addEventListener('DOMContentLoaded', function() {
    const cinemaBlocks = document.querySelectorAll('.cinema-block');
    const selectedCinemaIdInput = document.getElementById('selectedCinemaId');
    const buyTicketButton = document.getElementById('buyTicketButton');
    const movieId = buyTicketButton.getAttribute('data-movie-id');
    const showtimeSelection = document.getElementById('showtimeSelection');
    const showtimeBlocks = showtimeSelection.querySelectorAll('.showtime-block');

    cinemaBlocks.forEach(block => {
        block.addEventListener('click', function() {
            // Удаляем класс выделения у всех блоков
            cinemaBlocks.forEach(b => b.classList.remove('selected'));

            // Добавляем класс выделения к текущему блоку
            this.classList.add('selected');

            // Сохраняем ID выбранного кинотеатра
            const cinemaId = this.getAttribute('data-cinema-id');
            selectedCinemaIdInput.value = cinemaId;

            // Отображаем сеансы для выбранного кинотеатра
            showtimeSelection.style.display = 'block';
            showtimeBlocks.forEach(showtimeBlock => {
                if (showtimeBlock.getAttribute('data-cinema-id') === cinemaId && showtimeBlock.getAttribute('data-movie-id') === movieId) {
                    showtimeBlock.style.display = 'block'; // Показываем только соответствующие сеансы
                } else {
                    showtimeBlock.style.display = 'none'; // Скрываем остальные
                }
            });

            // Обновляем URL кнопки "Купить"
            buyTicketButton.href = `/orders/${movieId}/${cinemaId}/`; // Формируем URL
        });
    });

    showtimeBlocks.forEach(block => {
        block.addEventListener('click', function() {
            // Удаляем класс выделения у всех блоков
            showtimeBlocks.forEach(b => b.classList.remove('selected'));

            // Добавляем класс выделения к текущему блоку
            this.classList.add('selected');

            // Сохраняем ID выбранного сеанса
            const showtimeId = this.getAttribute('data-showtime-id');
            buyTicketButton.href = `/orders/${movieId}/${selectedCinemaIdInput.value}/${showtimeId}/`; // Обновляем URL с учетом сеанса
        });
    });

    buyTicketButton.addEventListener('click', function(event) {
        // Проверяем, выбран ли кинотеатр и сеанс
        if (!selectedCinemaIdInput.value || !document.querySelector('.showtime-block.selected')) {
            event.preventDefault(); // Отменяем отправку формы
            alert('Пожалуйста, выберите кинотеатр и сеанс перед покупкой билета.');
        }
    });
});
