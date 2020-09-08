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
print("Постарайтесь отгадать его за три попытки.\n")

# Начальные значения
the_number = random.randint(1, 100)
guess = int(input("Ваше предположение: "))
tries = 3

# Цикл отгадывания

while guess != the_number:
    if guess > the_number:
        print("Меньше", "у вас осталось", tries - 1, "попыток!")
    else:
        print("Больше", "у вас осталось", tries - 1, "попыток!")
    guess = int(input("Ваше предположение: "))
    tries -= 1
    if tries == 1:
        print("Fuck!", "Вы израсходовали свои попытки!")
        break
    if guess == the_number:
        print("Вам удалось отгадать число! Это в самом деле", the_number)
        input("\nНажмите Enter, чтобы выйти.")


