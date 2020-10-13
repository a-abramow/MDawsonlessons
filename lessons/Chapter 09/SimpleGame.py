# Простая игра
# Демонстрирует импорт модулей
from . import games
"""если модуль лежит в корневой папке, при импорте добавить {from .}"""
import random

print("Добро пожаловать в самую-самую простую игру!\n")

again = None
while again != "n":
    players = []
    num = games.ask_number(question="Сколько игроков участвует? (2 - 5):", low=2, high=5)
