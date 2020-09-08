cost = input("За какую стоимость Вы хотели бы продать свой автомобиль?")
cost = int(cost)
tax = int((cost / 100) * 13)
reg = int((cost / 100) * 1)
agent = int(750)
delivery = int(1500)

total = cost + tax + reg + agent + delivery

print("\nИтоговая стоимость автомобиля через наш сервис составит", total, " $.")
