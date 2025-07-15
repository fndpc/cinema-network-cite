document.addEventListener("DOMContentLoaded", () => {
  // Получаем все кнопки для отображения карты
  const mapButtons = document.querySelectorAll(".map-button")
  const mapModal = document.getElementById("myModal")
  const closeModal = document.querySelector(".close")
  let map = null
  let marker = null
  const ymaps3 = window.ymaps3 // Declare the ymaps3 variable

  // Функция для инициализации карты
  async function initMap(coords) {
    await ymaps3.ready
    const { YMap, YMapDefaultSchemeLayer, YMapMarker, YMapDefaultFeaturesLayer } = ymaps3

    // Если карта уже существует, уничтожаем ее
    if (map) {
      map.destroy()
    }

    // Создаем новую карту
    map = new YMap(document.getElementById("map"), {
      location: {
        center: coords,
        zoom: 14,
      },
    })

    const createMarker = () => {
      const markerContainerElement = document.createElement("div")
      markerContainerElement.classList.add("marker-container")

      const markerText = document.createElement("div")
      markerText.classList.add("marker-text", "hidden")
      markerText.innerText = "Кинотеатр"

      markerContainerElement.onmouseover = () => {
        markerText.classList.replace("hidden", "visible")
      }

      markerContainerElement.onmouseout = () => {
        markerText.classList.replace("visible", "hidden")
      }

      const markerElement = document.createElement("div")
      markerElement.classList.add("marker")

      const markerImage = document.createElement("img")
      markerImage.src = "/static/cinemas/js/icon.png"
      markerImage.classList.add("marker-image")

      markerElement.appendChild(markerImage)
      markerContainerElement.appendChild(markerText)
      markerContainerElement.appendChild(markerElement)

      return new YMapMarker(
        {
          coordinates: coords,
        },
        markerContainerElement,
      )
    }

    marker = createMarker()

    map.addChild(new YMapDefaultSchemeLayer())
    map.addChild(new YMapDefaultFeaturesLayer())
    map.addChild(marker)
  }

  // Обработчик клика по кнопке "Показать на карте"
  mapButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const coordinates = JSON.parse(this.getAttribute("data-coordinates"))
      mapModal.style.display = "block"
      document.body.style.overflow = "hidden"

      // Инициализируем карту с задержкой, чтобы она корректно отобразилась
      setTimeout(() => {
        initMap(coordinates)
      }, 100)
    })
  })

  // Закрытие модального окна
  closeModal.addEventListener("click", () => {
    mapModal.style.display = "none"
    document.body.style.overflow = ""
  })

  // Закрытие модального окна при клике вне его содержимого
  mapModal.addEventListener("click", (event) => {
    if (event.target === mapModal) {
      mapModal.style.display = "none"
      document.body.style.overflow = ""
    }
  })

  // Закрытие модального окна по нажатию Escape
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && mapModal.style.display === "block") {
      mapModal.style.display = "none"
      document.body.style.overflow = ""
    }
  })
})
