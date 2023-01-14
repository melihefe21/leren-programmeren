from random import randint

kleur = ['oranje','blauw','groen','bruin']
vraag = int(input("hoeveel m&m's wil je"))
leeg= []



for x in range(vraag):
    random = randint(0,3)
    random_num = kleur[random]
    leeg.append(random_num)



print(leeg)
