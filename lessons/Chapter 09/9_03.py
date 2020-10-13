# Карты 2.0
# Демонстрирует расширение классов через наследование


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


class Hand(object):
    """Рука: набор карт на руках одного игрока."""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<пусто>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """Колода игральных карт"""

    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Не могу больше сдавать: карты закончились!")


# основная часть
deck1 = Deck()
print("Создана новая колода.")
print("Вот эта колода:")
print(deck1)
deck1.populate()
print("В колоде появились карты.")
print("Вот как колода выглядит теперь:")
print(deck1)
deck1.shuffle()
print("Перетасуем карты в колоде")
print("Вот как они теперь выглядят: ")
print(deck1)
my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]
deck1.deal(hands, per_hand=5)
print("\nМне и Вам на руки выдано по 5 карт.")
print("\nВот, что у Вас на руках.")
print(your_hand)
print("\nВот, что у меня на руках.")
print(my_hand)
print("\nОсталось в колоде:")
print(deck1)
deck1.clear()
print("\nКолода очищена")
print("Вот как она выглядит теперь:", deck1)
input("\n\nНажмите Enter, чтобы выйти.")




# card1 = Card(rank="Т", suit="к")
# print("Вывожу на экран объект-карту:")
# print(card1)
# card2 = Card(rank="2", suit="к")
# card3 = Card(rank="3", suit="к")
# card4 = Card(rank="4", suit="к")
# card5 = Card(rank="5", suit="к")
# print("\nВывожу еще четыре карты:")
# print(card2)
# print(card3)
# print(card4)
# print(card5)
# my_hand = Hand()
# print("\nПечатаю карты, которые у меня на руках до раздачи: ")
# print(my_hand)
# my_hand.add(card1)
# my_hand.add(card2)
# my_hand.add(card3)
# my_hand.add(card4)
# my_hand.add(card5)
# print("\nПечатаю карты, которые появились у меня на руках: ")
# print(my_hand)
# your_hand = Hand()
# my_hand.give(card1, your_hand)
# my_hand.give(card2, your_hand)
# print("\nПечатаю карты, которые остались у меня на руках: ")
# print(my_hand)
# print("\nПечатаю карты, которые появились у Вас на руках: ")
# print(your_hand)
# my_hand.clear()
# print("\nУ меня на руках после того как сбросил: ")
# print(my_hand)
# input("\n\nНажмите Enter, чтобы выйти.")
