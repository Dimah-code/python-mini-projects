from random import randint


def main():
    questions_key = create_questions()

    answers = create_questions()

    score = calculate_score(questions_key, answers)

    print("=" * 20 + "RANDOM ANSWERS" + "=" * 20)
    print(score)

    questions = create_questions()
    answer = 3

    score = calculate_onlyone_answer(questions, answer)
    print("=" * 20 + "ONLY ONE ANSWER" + "=" * 20)
    print(score)


def create_questions() -> list[int]:
    questions_key: list[int] = []

    for _ in range(20):
        key = randint(1, 4)
        questions_key.append(key)
    return questions_key


def calculate_score(questions_key, answers) -> int:
    score: int = 0
    for key in questions_key:
        if key == answers[key]:
            score += 1
    return score


def calculate_onlyone_answer(questions, answer):
    score: int = 0
    for i in questions:
        if answer == questions[i]:
            score += 1
    return score


if __name__ == "__main__":
    main()
