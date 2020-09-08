# Демонстрируется работа составных условий и логических операторов
print("\t\tЭксклюзивная компьютерная сеть")
print("\tТолько для зарегистрированных пользователей!\n")
security = 0
username = ""
while not username:
    username = input("Логин: ")
password = ""
while not password:
    password = input("Пароль: ")

if username == "Abramov-A" and password == "123123":
    print("Привет, Андрюх!")
    security = 5
elif username == "S.Meier" and password == "civil":
    print("Здравствуй, Сид!")
    security = 3
elif username == "S.Miyamoto" and password == "mario":
    print("Доброго времени суток, Сигеру!")
    security = 3
elif username == "W.Wright" and password == "thesims":
    print("как дела, Уилл?")
    security = 3
elif username == "guest" or password == "guest":
    print("Добро пожаловать к нам в гости.")
    security = 1
else:
    print("Войти в систему не удалось. Должно быть, вы не из нашего клуба.\n")
input("\n\nНажмите Enter чтобы выйти.")
