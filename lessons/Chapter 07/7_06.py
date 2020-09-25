# Обработаем
# Демонстрирует обработку нескольких исключений
# try/except

print()
for value in (None, "Привет!"):
    try:
        print("Пытаюсь преобразовать в число: ", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Я могу преобразовывать только строки и числа!")
    except ValueError:
        print("Я могу преобразовывать только строки, состоящие из цифр!")
