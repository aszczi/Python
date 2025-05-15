import os
import random
import datetime

answers = [
    "Nie sądzę.",
    "Oczywiście, że tak!",
    "Nie wiem.",
    "Zapytaj ponownie później.",
    "Na pewno nie!",
    "Jest to prawdopodobne.",
    "Wszystko wskazuje na tak.",
    "Możliwe.",
    "Wątpliwe.",
    "Bez wątpienia!",
    "Nie licz na to.",
    "To pewne!"
]
today_date = datetime.date.today()


def get_random_answer(answers):
    return random.choice(answers)



def check_location():
    if not os.path.exists(os.path.join(os.getcwd(), "QA")):
        os.mkdir(os.path.join(os.getcwd(), "QA"))
        print("Creating location for saving answers")

def load_answer(path=None):
    if path != None:
        if os.path.exists(path):
            with open(path, "r") as r_answer:
                for r in r_answer.readlines():
                    answers.append(r)
    return answers

def save_question_and_answer(question, answer):
    check_location()
    with open(os.path.join("QA", f"{today_date}.txt"), "a+") as w_answer:
        w_answer.write(f"{question} : {answer}\n")


def play_game(answers):
    question = input("Ask anything:\n")
    answer = get_random_answer(answers)
    print(f"{answer}\n")
    save_question_and_answer(question, answer)


if __name__ == "__main__":
    print(today_date)
    play_game(answers)

