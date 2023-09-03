import telebot
import schedule
import time
from get_news import get_news
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
channel_id = '@tgUKRAINEnews'

texts = []
def send_notification():
    text = f'{get_news(detailed=True)}'
    url = f'{get_news(href=True)}'
    if text not in texts:
        bot.send_message(channel_id, f'{text}\n<a href="{url}">Читати детальніше</a>', parse_mode='HTML')
        texts.append(text)

@bot.message_handler(commands=['start'])
def start(message):
    cht = message.chat.id
    try:
        bot.send_message(cht, 'started')
        schedule.every(5).seconds.do(send_notification)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as ex:
        bot.send_message(cht, ex)
bot.polling()