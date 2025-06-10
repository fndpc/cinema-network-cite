import telebot
from urllib.parse import quote
from django.conf import settings
import requests

API_TOKEN = "8150817803:AAFuhvfZ_udCiLU_IVUGZkTmOk4VdFR3cz4"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, это бот для отслеживания статистики кинотеатров")

@bot.message_handler(commands=['id'])
def send_welcome(message):
    bot.reply_to(message, message.chat.id)

def send_notiflication(order):
    message = quote(f"Новый заказ: {order.showtime} {order.user}")
    url = f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage?chat_id={settings.CHAT_ID}&text={message}"
    print(requests.get(url))



# bot.infinity_polling()