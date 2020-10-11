# Гибель пришельца
# Демострирует взаимодействие объектов


class Player(object):
    """Игрок в экшен-игре"""

    def blast(self, enemy):
        self.is_not_used()
        print("Игрок стреляет во врага.\n")
        enemy.die()

    def is_not_used(self):
        pass


class Alien(object):
    """Врождебный пришелец-инопланетянин в экшен-игре"""

    def die(self):
        self.is_not_used()
        print("Тяжело дыша, пришелец погибает от рук героя...\n")

    def is_not_used(self):
        pass

# Основная часть программы


print("\t\tГибель пришельца\n")
hero = Player()
invader = Alien()
hero.blast(invader)
input("\n\nНажмите Enter, чтобы выйти.")
