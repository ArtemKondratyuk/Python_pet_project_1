import json
import random

def load_phrases(filename="phrases.json"):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def get_randome_phrase(mood, data):
    mood = mood.strip().lower()
    if mood in data:
        return random.choice(data[mood])
    return "Такого настроения Я не знаю. Хорошего тебе дня!"

data = load_phrases()

while True:
    mood = input("Укажите свое настроение (очень плохое, плохое, так себе):").strip().lower()

    phrase = get_randome_phrase(mood, data)

    print(phrase)

    repeat = input("Хотите попробовать снова? (да/нет): ").strip().lower()

    if repeat != "да":
        print("Досвидания! Хорошего настроения тебе!")
        break  