print(
    """
            Рантье
    
    Программа подсчитывает Ваши ежесемячные расходы. Эту статистику нужно знать, чтобы у вас не закончились деньги и Вам
    не пришлось бы искать работу.
    Введите суммы расходов по всем статьям, перечисленным ниже. Вы богаты - так не мелочитесь, пишите суммы в долларах,
    без центов.
    
    """
)

car = int(input("Техническое обслуживание машины 'Chevrolet': "))
rent = int(input("Съем роскошной квартиры на Лесной: "))
jet = int(input("Аренда самолета: "))
gifts = int(input("Подарки: "))
food = int(input("Обеды и ужины в ресторанах: "))
staff = int(input("Жалование прислуги(дворецкий, водитель, повар, секретарь): "))
guru = int(input("Оплата личному психоаналитику: "))
games = int(input("Компьютерные игры: "))
total = car + rent + jet + gifts + food + staff + guru + games
print("\nОбщая сумма: ", total)
input("\nНажмите Enter, чтобы выйти.")
