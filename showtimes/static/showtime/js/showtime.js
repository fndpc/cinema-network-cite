
        document.addEventListener('DOMContentLoaded', function () {
            const dateInput = document.getElementById('date-input');
            const today = new Date().toISOString().split('T')[0];
            dateInput.setAttribute('min', today); // Устанавливаем минимальную дату на сегодня

            // Добавляем обработчик для красивого отображения календаря
            dateInput.addEventListener('focus', function () {
                this.showPicker();
            });
        });
