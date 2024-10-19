
def calculate_score(answers, correct_answers):
    score = sum(1 for answer, correct in zip(answers, correct_answers) if answer == correct)
    return score
