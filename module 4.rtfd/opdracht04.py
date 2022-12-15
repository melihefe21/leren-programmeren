from fruitmand import fruitmand
import random
x = int(input('hoeveel fruit?'))
for i in range(x):
    fruit_naam = random.choice(fruitmand)
    print(fruit_naam['name'])

