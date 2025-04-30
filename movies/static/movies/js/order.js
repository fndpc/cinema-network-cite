document.addEventListener('DOMContentLoaded', function() {
    // Получаем все блоки кинотеатров
    const cinemaBlocks = document.querySelectorAll('.cinema-block');
    const showtimeSelection = document.getElementById('showtimeSelection');
    const selectedShowtimeId = document.getElementById('selectedShowrtimeId');

    // Скрываем блок сеансов изначально
    showtimeSelection.style.display = 'none';

    // Добавляем обработчик события для каждого блока кинотеатра
    cinemaBlocks.forEach(block => {
        block.addEventListener('click', function() {
            // Получаем ID выбранного кинотеатра
            const selectedCinemaId = this.getAttribute('data-cinema-id');
            const showtimeBlocks = document.querySelectorAll('.showtime-block');

            // Скрываем все сеансы
            showtimeSelection.style.display = 'none';

            // Убираем выделение у всех блоков кинотеатров
            cinemaBlocks.forEach(b => b.classList.remove('selected'));

            // Выделяем выбранный блок кинотеатра
            this.classList.add('selected');

            // Показываем только сеансы, связанные с выбранным кинотеатром
            let hasShowtimes = false;
            showtimeBlocks.forEach(showtime => {
                if (showtime.getAttribute('data-cinema-id') === selectedCinemaId) {
                    showtime.style.display = 'block';
                    hasShowtimes = true;
                } else {
                    showtime.style.display = 'none';
                }
            });

            // Если есть сеансы, показываем блок сеансов
            if (hasShowtimes) {
                showtimeSelection.style.display = 'block';
            } else {
                showtimeSelection.style.display = 'none';
            }
        });
    });

    // Добавляем обработчик события для сеансов
    const showtimeBlocks = document.querySelectorAll('.showtime-block');
    showtimeBlocks.forEach(showtime => {
        showtime.addEventListener('click', function() {
            // Получаем ID выбранного сеанса
            const selectedId = this.getAttribute('data-showtime-id');
            selectedShowtimeId.value = selectedId;

            // Убираем выделение у всех блоков сеансов
            showtimeBlocks.forEach(s => s.classList.remove('selected'));

            // Выделяем выбранный блок сеанса
            this.classList.add('selected');
        });
    });
});
