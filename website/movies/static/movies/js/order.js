document.addEventListener("DOMContentLoaded", () => {
  // Получаем элементы
  const cinemaBlocks = document.querySelectorAll(".cinema-block-movie-order");
  const showtimeBlocks = document.querySelectorAll(".showtime-block-movie-order");
  const showtimeSelection = document.getElementById("showtimeSelection-movie-order");
  const selectedShowtimeIdInput = document.getElementById("selectedShowrtimeId");
  const orderForm = document.getElementById("orderForm");
  const cinemaError = document.getElementById("cinemaError");
  const showtimeError = document.getElementById("showtimeError");

  // Переменные для хранения выбранных значений
  let selectedCinemaId = null;
  let selectedShowtimeId = null;

  // Обработчик выбора кинотеатра
  cinemaBlocks.forEach((block) => {
    block.addEventListener("click", function () {
      // Удаляем класс selected у всех блоков кинотеатров
      cinemaBlocks.forEach((b) => b.classList.remove("selected"));

      // Добавляем класс selected текущему блоку
      this.classList.add("selected");

      // Получаем ID выбранного кинотеатра
      selectedCinemaId = this.getAttribute("data-cinema-id");
      cinemaError.style.display = "none";

      // Показываем блок выбора сеансов
      showtimeSelection.style.display = "grid";

      // Фильтруем сеансы по выбранному кинотеатру
      showtimeBlocks.forEach((showtime) => {
        if (showtime.getAttribute("data-cinema-id") === selectedCinemaId) {
          showtime.style.display = "block";
        } else {
          showtime.style.display = "none";
        }
      });

      // Сбрасываем выбор сеанса
      showtimeBlocks.forEach((b) => b.classList.remove("selected"));
      selectedShowtimeId = null;
      selectedShowtimeIdInput.value = "";
    });
  });

  // Обработчик выбора сеанса
  showtimeBlocks.forEach((block) => {
    block.addEventListener("click", function () {
      // Удаляем класс selected у всех блоков сеансов
      showtimeBlocks.forEach((b) => b.classList.remove("selected"));

      // Добавляем класс selected текущему блоку
      this.classList.add("selected");

      // Получаем ID выбранного сеанса и сохраняем в скрытое поле
      selectedShowtimeId = this.getAttribute("data-showtime-id");
      selectedShowtimeIdInput.value = selectedShowtimeId;
      showtimeError.style.display = "none";
    });
  });

  // Валидация формы перед отправкой
  orderForm.addEventListener("submit", (e) => {
    // Проверяем, выбран ли сеанс
    if (!selectedShowtimeId) {
      e.preventDefault(); // Предотвращаем отправку формы
      showtimeError.style.display = "inline"; // Показываем ошибку

      // Прокручиваем к блоку выбора сеанса
      document.querySelector("#showtimeSelection-movie-order").scrollIntoView({
        behavior: "smooth",
        block: "center"
      });
      return; // Прерываем выполнение
    }

    // Проверяем, выбран ли кинотеатр
    if (!selectedCinemaId) {
      e.preventDefault(); // Предотвращаем отправку формы
      cinemaError.style.display = "inline"; // Показываем ошибку

      // Прокручиваем к блоку выбора кинотеатра
      document.querySelector("#cinemaSelection-movie-order").scrollIntoView({
        behavior: "smooth",
        block: "center"
      });
      return; // Прерываем выполнение
    }
  });

  // Анимация появления элементов при прокрутке
  const animateOnScroll = () => {
    const elements = document.querySelectorAll(
      ".movie-block-movie-order, .cinema-block-movie-order, .showtime-block-movie-order",
    );

    elements.forEach((element) => {
      const elementPosition = element.getBoundingClientRect().top;
      const screenPosition = window.innerHeight / 1.3;

      if (elementPosition < screenPosition) {
        element.style.opacity = "1";
        element.style.transform = "translateY(0)";
      }
    });
  };

  // Инициализация стилей для анимации
  const initAnimationStyles = () => {
    const elements = document.querySelectorAll(
      ".movie-block-movie-order, .cinema-block-movie-order, .showtime-block-movie-order",
    );

    elements.forEach((element, index) => {
      element.style.opacity = "0";
      element.style.transform = "translateY(20px)";
      element.style.transition = "opacity 0.5s ease, transform 0.5s ease";
      element.style.transitionDelay = `${index * 0.05}s`;
    });
  };

  // Инициализируем стили
  initAnimationStyles();

  // Запускаем анимацию при загрузке и прокрутке
  window.addEventListener("scroll", animateOnScroll);
  window.addEventListener("load", animateOnScroll);
});