# Создайте программу, которая будет выводить список слов в случайном порядке.На экране должны печататься без
# повторений все слова из представленного списка.

import random
words = ["run", "fast", "bill", "apple", "dog", "cat"]

print('Эти слова в случайном порядке:')

while words:
    word = random.choice(words)
    print(word)
    words.remove(word)
