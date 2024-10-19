
import time

def start_timer(duration, bot, chat_id):
    time.sleep(duration)
    bot.send_message(chat_id, "Время вышло! Пожалуйста, завершите ваш квиз.")
