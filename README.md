# Веб приложение для администрирования сети кинотеатров

## Версия без поддержки Telegram-бота (версия с ботом - [GitHub репозиторий](https://github.com/fndpc/cinema-network-cite/tree/feat/DEV-666-add-telegrambot-notiflicatons))

Запуск локального серевера:
1. Создать виртуальое окружение в каталоге с каталогом проекта (опционально):
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
YMAPS_API_KEY='нужно получить на сайте https://developer.tech.yandex.ru/services'

TIME_ZONE='Europe/Moscow'
LANGUAGE_CODE='ru'
```
5. Запустить сервер
   ```python manage.py runserver```

Для авторизации можно использовать профиль администрации
   login: admin
   pass: 12345

Страница админки находится по адресу localhost:8000/admin
