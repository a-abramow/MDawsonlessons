# Моя зверюшка
# Виртуальный питомец, о котором пользователь может заботиться

class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
