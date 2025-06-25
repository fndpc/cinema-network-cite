// Получаем элементы
var modal = document.getElementById("myModal");
var span = document.getElementsByClassName("close")[0];
var buttons = document.getElementsByClassName("map-button");

let map;
for (let i = 0; i < buttons.length; i++) {
    buttons[i].onclick = function() {
        // Получаем координаты из атрибута data
        const coordinates = JSON.parse(this.getAttribute('data-coordinates'));
        initMap(coordinates);
        modal.style.display = "block";
    }
}

// Когда пользователь нажимает на (x), закрываем окно
span.onclick = function() {
    modal.style.display = "none";
}

// Когда пользователь нажимает в любом месте вне окна, закрываем его
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


// СОЗДАНИЕ КАРТЫ
async function initMap(coords) {
    await ymaps3.ready;
    const {YMap, YMapDefaultSchemeLayer, YMapMarker, YMapDefaultFeaturesLayer} = ymaps3;

    // Если карта уже существует, уничтожаем ее
    if (map) {
        map.destroy();
    }

    // Создаем новую карту
    map = new YMap(
        document.getElementById('map'),
        {
            location: {
                center: coords,
                zoom: 14
            }
        }
    );

    const createMarker = () => {
        const markerContainerElement = document.createElement('div');
        markerContainerElement.classList.add('marker-container');
    
        const markerText = document.createElement('div');
        // markerText.id = feature.id;
        markerText.classList.add('marker-text', 'hidden');
        // markerText.innerText = NAMES[feature.id];
    
        markerContainerElement.onmouseover = () => {
            markerText.classList.replace('hidden', 'visible');
        };
    
        markerContainerElement.onmouseout = () => {
            markerText.classList.replace('visible', 'hidden');
        };
    
        const markerElement = document.createElement('div');
        markerElement.classList.add('marker');
    
        const markerImage = document.createElement('img');
        markerImage.src = '/static/cinemas/js/icon.png';
        markerImage.classList.add('marker-image');
    
        markerElement.appendChild(markerImage);
        markerContainerElement.appendChild(markerText);
        markerContainerElement.appendChild(markerElement);
    
        return new YMapMarker(
            {
                coordinates: coords
            },
            markerContainerElement
        );
    };

    marker = createMarker()

    map.addChild(new YMapDefaultSchemeLayer());
    map.addChild(new YMapDefaultFeaturesLayer());
    map.addChild(marker)    
}
