
from database import get_results

def get_user_quiz_history(user_id):
    return get_results(user_id)
