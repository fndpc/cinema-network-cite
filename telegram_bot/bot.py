import asyncio
import logging
import sys
import aio_pika
import json
import db
import os
from dotenv import load_dotenv


from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import FSInputFile


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
RABBITMQ_URL = "amqp://guest:guest@localhost/"
dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    token = message.text.split()[1] if len(message.text.split()) > 1 else None
    if token:
        if not db.check_id_in_db(token=token, chat_id=message.chat.id)[0]:
            await message.answer("Вы успешно привязали свой Telegram")
        else:
            await message.answer(
            f"Ваш Telegram-аккаунт уже привязан."
        )
    else:
        await message.answer(
            f"Привет, {html.bold(message.from_user.full_name)}! "
            f"Этот бот отправляет билеты после их покупки на сайте нашего кинотеатра. "
            f"Перейдите по адресу localhost:8000 и не забудьте привязать ваш Telegram-аккаунт в профиле."
        )


async def on_message(message: aio_pika.IncomingMessage) -> None:
    async with message.process():
        data = json.loads(message.body.decode('utf-8'))
        path = data['qr_path']
        chat_id = data['telegram_chat_id']
        qr = FSInputFile(path)
        text = """
                Благодарим вас за приобритение билета в CINEMA ПАРК :)\nЖелаем вам приятного посещения ❤
               """
        await bot.send_photo(chat_id, photo=qr, caption=text)


async def consume_queue():
    try:
        connection = await aio_pika.connect_robust(RABBITMQ_URL)
        async with connection:
            channel = await connection.channel()
            queue = await channel.declare_queue('orders', durable=True)
            await queue.consume(on_message)
            print("Начата обработка сообщений из очереди 'orders'")
            await asyncio.Future()
    except Exception as e:
        print(f"Ошибка в потребителе очереди: {e}")


async def main():
    tasks = [
        asyncio.create_task(dp.start_polling(bot)),
        asyncio.create_task(consume_queue())
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())