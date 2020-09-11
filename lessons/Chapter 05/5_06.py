# Рекорды
# Демонстрирует списочные методы

scores = []
choice = None

while choice != "0":
    print(
        """
        Рекорды
        0 - Выйти
        1 - Показать рекорды
        2 - Добавить рекорды
        3 - Удалить рекорды
        4 - Сортировать список
        """
    )
    choice = input("Ваш выбор: ")
    print()
    if choice == "0":
        print("Приходите еще! Пока!")
    elif choice == "1":
        print("Рекорды")
        for score in scores:
            print(score)
    elif choice == "2":
        score = int(input("Введите свой рекорд: "))
        scores.append(score)
    elif choice == "3":
        score = int(input("Какой из рекордов удалить?: "))
        if score in scores:
            scores.remove(score)
        print("Результат", score, "не содержится в списке рекордов.")
    elif choice == "4":
        scores.sort(reverse=True)
    else:
        print("Извините, в меню нет пункта", choice)
