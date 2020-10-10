# Зверюшка со свойствами
# Демонстрирует свойства


class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == " ":
            print("Имя зверюшки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно заменено!")

    def talk(self):
        print("\nПривет, меня зовут ", self.name)

# Основная часть

crit = Critter("Бобик")
crit.talk()

print("\nМою зверюшку зовут", end=" ")
print(crit.name)





