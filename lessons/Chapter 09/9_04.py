# Карты 3.0
# Демонстрирует наследование в части переопределения методов


class Card(object):
    """Одна игральная карта"""

    RANKS = ["Т", "2", "3", "4", "5", "6", "7", "8", "9", "10", "В", "Д", "К"]
    SUITS = ["к", "п", "б", "ч"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class UnprintableCard(Card):
    """Карта, номинал и масть которой не могут быть выведены на экран"""

    def __str__(self):
        return "<нельзя напечатать>"


class PositionableCard(Card):
    """Карта, которую можно положить лицом или рубашкой вверх."""

    def __init__(self, rank, suit, face_up=True):
        super(PositionableCard, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(PositionableCard, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


# основная часть


card1 = Card("Т", "ч")
card2 = UnprintableCard("Т", "б")
card3 = PositionableCard("Т", "п")
print("Печатаю объект Card:")
print(card1)
print("\nПечатаю объект UnprintableCard:")
print(card2)
print("\nПечатаю объект PositionableCard:")
print(card3)
print("\nПереворачиваю объект PositionableCard:")
card3.flip()
print("\nПечатаю объект PositionableCard:")
print(card3)
input("\n\nНажмите Enter, чтобы выйти.")
