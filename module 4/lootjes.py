from random import shuffle
namen_lijst = []
aantal_namen = 0
meer_namen = True
Koppelen = False

while meer_namen or aantal_namen < 3:
    if aantal_namen >= 3:
        print('Typ "stop" om het programma te stoppen, of voeg nieuwe namen toe!')
    namen_input = input('Voer een naam in: ').capitalize()
    if namen_input == 'Stop' and aantal_namen >= 3:
        meer_namen = False
    elif namen_input in namen_lijst:
        print('Deze naam bestaat al in de lijst.')
    else:
        namen_lijst.append(namen_input)
        aantal_namen += 1

namen_lijst2 = [] + namen_lijst
while not Koppelen:
    shuffle(namen_lijst)
    Koppelen = True
    for x in range(0,len(namen_lijst2)):
        if namen_lijst[x] == namen_lijst2[x]:
            test = False
for x in range(0,len(namen_lijst2)):
    print(f'{namen_lijst[x]} heeft {namen_lijst2[x]} getrokken')