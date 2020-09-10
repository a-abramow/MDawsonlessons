# Арсенал героя
# Демонстрирует создание кортежа

inventory = ()
if not inventory:
    print("Вы безоружны.")
input("\n\nНажмите Enter, чтобы выйти.")

inventory = ("меч",
             "кольчуга",
             "щит",
             "целебное снадобье")

print("\nСодержимое кортежа: ")
print(inventory)

print("\nИтак, в вашем арсенале: ")

for item in inventory:
    print(item)

input("\n\nНажмите Enter, чтобы выйти.")
