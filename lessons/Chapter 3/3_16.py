# Отгадай число
#
# Компьютер выбирает случайное число в диапазоне от 1 до 100
# Игрок пытается отгадать это число и компьютер говорит
# предположение больше\меньше, чем загаданное число
# или попало в точку

import random

# Приветствие и правила игры
print("\tДобро пожаловать в игру 'Отгадай число'!")
print("\nЯ загадал натуральное число из диапазона от 1 до 100.")
print("Постарайтесь отгадать его за минимальное число попыток.\n")

# Начальные значения
the_number = random.randint(1, 100)
guess = int(input("Ваше предположение: "))
tries = 1

# Цикл отгадывания

while guess != the_number:
    if guess > the_number:
        print("Меньше")
    else:
        print("Больше")
    guess = int(input("Ваше предположение: "))
    tries += 1

print("Вам удалось отгадать число! Это в самом деле", the_number)
print("Вы затратили на отгадывание всего лишь", tries, "попыток!\n")
input("\nНажмите Enter, чтобы выйти.")
