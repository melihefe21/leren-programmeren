import random 

kleur = ['oranje','blauw','groen','bruin']
leeg= {}

vraag = int(input("hoeveel= "))

for i in range(vraag):
    k = random.randint(0, len(kleur)-1)
    if kleur[k] not in leeg:
        leeg.update({kleur[k]: 1})
    else:
        i = leeg.get(kleur[k]) + 1
        leeg.update({kleur[k]: i})

print(leeg)