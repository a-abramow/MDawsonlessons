# Считалка
# Демонстрирует использование функции range()
print("Посчитаем!")
for i in range(10):
    print(i, end=" ")
print("\nПересчитаем кратные пяти: ")
for i in range(0, 50, 5):
    print(i, end=" ")
print("\nПересчитаем в обратной последовательности: ")
for i in range(10, 0, -1):
    print(i, end=" ")

