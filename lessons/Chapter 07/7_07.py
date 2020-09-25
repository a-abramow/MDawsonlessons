# Викторина
# Игра на выбор правильного ответа.
# вопросы из которого читаются из текстового файла


import sys


def open_file(testf, mode):
    try:
        the_file = open(testf, mode, encoding='utf-8')
    except IOError as e:
        print("Невозможно открыть файл", testf, "Работа программы будет завершена.\n", e)
        input("Нажмите Enter, чтобы выйти!")
        sys.exit()
    else:
        return the_file
