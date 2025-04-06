import tkinter as tk
from tkinter import messagebox
import json
import random

def load_phrases(filename="phrases.json"):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def get_random_phrase(mood, data):
    mood = mood.strip().lower()
    if mood in data:
        return random.choice(data[mood])
    return "Такого настроения я не знаю. Но хорошего тебе настроения!"

# Создаем основное окно 
root = tk.Tk()
root.title("Генератор фраз для поднятия настроения") # Заголовок окна
root.geometry("500x400")  # Размер окна

mood_label = tk.Label(text="Введите ваше настроение:")
