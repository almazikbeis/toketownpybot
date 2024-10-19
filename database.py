
import sqlite3

def init_db():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS results (user_id INTEGER, quiz_topic TEXT, score INTEGER)''')
    conn.commit()
    conn.close()

def save_result(user_id, quiz_topic, score):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO results (user_id, quiz_topic, score) VALUES (?, ?, ?)", (user_id, quiz_topic, score))
    conn.commit()
    conn.close()

def get_results(user_id):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT quiz_topic, score FROM results WHERE user_id=?", (user_id,))
    results = cursor.fetchall()
    conn.close()
    return results
