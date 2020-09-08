# Напишите программу, симулятор пирожка с сюрпризом, - которая бы при запуске отображала один из пяти различных
# сюрпризов, выбранный случайным образом.

import random

surprise = random.randint(1, 5)
if surprise == 1:
    print("apple")
elif surprise == 2:
    print("meat")
elif surprise == 3:
    print("honey")
elif surprise == 4:
    print("strawberry")
else:
    print("pineapple")


