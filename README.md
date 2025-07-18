# Веб приложение для администрирования сети кинотеатров

Запуск локального серевера:
1. Создать виртуальое окружение в каталоге с каталогом сайта (опционально):
   ```python -m venv venv```
2. Перейти в каталог проекта:
   ```cd cinema-network-cite```
3. Установить зависимости
   ```pip install -r requirements.txt```
4. Установить переменные окружения (создать .env)
```
SECRET_KEY='рандомный ключ'
DEBUG=True
ALLOWED_HOSTS=127.0.0.1 localhost

TIME_ZONE='Europe/Moscow'
LANGUAGE_CODE='ru'
```
5. Запустить сервер
   ```python manage.py runserver```

1. **Создание бота**:
   - Создайте бота через [BotFather](https://t.me/BotFather)
   
2. **Настройка окружения**:
   - В файле `.env` в корневом каталоге проекта укажите:
     ```ini
     BOT_TOKEN='ваш_токен'
     ```
3. **Запуск бота**:
   - Запустите сайт командой ```python manage.py runserver```

4. **Получение Chat ID**:
   - Отправьте команду `/id` вашему боту
   - Скопируйте полученный ID
   - Добавьте в `.env` файл:
     ```ini
     CHAT_ID='ваш_chat_id'
     ```
     
Для авторизации можно использовать профиль администрации
   login: admin
   pass: 12345

Страница админки находится по адресу localhost/admin
