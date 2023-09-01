import telebot
import schedule
import time
from get_news import get_news
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
channel_id = '@tgnews228'

texts = []
def send_notification():
    text = f'{get_news(detailed=True)}'
    if text not in texts:
        bot.send_message(channel_id, text, parse_mode='HTML')
        texts.append(text)

@bot.message_handler(commands=['start'])
def start(message):
    schedule.every(5).seconds.do(send_notification)
    while True:
        schedule.run_pending()
        time.sleep(1)
bot.polling()