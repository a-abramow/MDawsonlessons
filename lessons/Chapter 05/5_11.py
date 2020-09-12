# Виселица
#
# классическая игра "Виселица". Компьютер случайным образом выбирает слово,
# которое игрок должен отгадать буква за буквой. Если игрок не сумеет
# отгадать за отведенное количество попыток, на экране появится фигурка повешенного
# импорт модуля

import random

# константы
HANGMAN = (
    """
    ------
    |
    |
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    O
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    O
    |    ^
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    O
    |    ^
    |    | 
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    O
    |    ^
    |    | 
    |    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    O
    |    ^
    |    | 
    |    |
    |   |
    |   |
    |
    ----------
    """,
    """
    ------
    |    |
    |    @
    |    ^
    |    | 
    |    |
    |   | |
    |   | |
    |
    ----------
    """)
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("ПРИВЕТ", "ПОКА", "ПИТОН", "СЕМИНАРИЯ", "ЗАПОВЕДЬ", "ПРОГРАММА", "РАБОТА")

word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

print("Добро пожаловать в игру 'Виселица'. Удачи Вам!")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nВы предлагали следующие буквы:\n", used)
    print("\nОтгаданное вами слово сейчас выглядит так:\n", so_far)

    guess = input("\n\nВведите букву: ")
    guess = guess.upper()
    while guess in used:
        print("Вы уже предлагали такую букву", guess)
        guess = input("\n\nВведите букву: ")
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print("\nДа! Буква", guess, " есть в слове!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\n К сожалению, буквы", guess, "нет в слове.")
        wrong += 1
    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("\nВас повесили!")
    else:
        print("\nВы отгадали!")
print("\nБыло загадано слово", word)
input("\n\nНажмите Enter, чтобы выйти.")

