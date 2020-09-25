# Обработаем
# Демонстрирует обработку исключительных ситуаций
# try/except


try:
    num = float(input("Введиет число: "))
except ValueError:
    print("Похоже, это не число!")

