
def collect_feedback(bot, chat_id, feedback_text):
    bot.send_message(chat_id, "Спасибо за ваш отзыв!")
    with open('feedback.txt', 'a') as file:
        file.write(f"Отзыв от {chat_id}: {feedback_text}\n")
