
import random

def generate_random_questions(topic):
    questions = [
        f"Что вы знаете о {topic}?",
        f"Какие ключевые концепции можно выделить в {topic}?",
        f"Как вы можете применить {topic} в реальной жизни?",
        f"Назовите три преимущества изучения {topic}.",
        f"Почему важно понимать {topic} в современных условиях?"
    ]
    return random.choice(questions)
