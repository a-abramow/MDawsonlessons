# Напишите программу, которая бы подбрасывала условую монету 100 раз и сообщала, скольк раз выпал орел, а сколько -
# решка

import random

heads = 0
tails = 0
i = 0

while i < 100:
    i += 1
    coin = random.randint(1, 2)
    if coin == 1:
        heads += 1
    else:
        tails += 1
    if i == 100:
        print("Орел выпал", heads, "раз")
        print("Решка выпала", tails, "раз")
