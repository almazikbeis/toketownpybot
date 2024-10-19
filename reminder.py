
import time

def send_reminder(chat_id, bot, interval, message):
    while True:
        time.sleep(interval)
        bot.send_message(chat_id, message)
