import random
import os

stop = False
punten = 0
game = 0
while game != 20 or stop == False:
    game =+ 1
    nummer = random.randint(1,1000)
    ronde = 0
    while ronde <= 10:
        ronde = ronde + 1
        Gok = int(input('Gok een getal tussen 1 en 1000.'))
        if Gok == nummer:
            punten += 1
            print('Goed gedaan! Je hebt 1 punt erbij!')
            os.system('cls')
        if nummer < Gok:
            print('<')
        elif nummer > Gok:
            print('>')
        verschil = nummer - Gok
        if verschil < 0:
            verschil *- 1
        if verschil <= 20:
            print('Je bent erg warm')
        elif verschil <= 50:
            print('Je bent warm')

        if ronde == 10:
            os.system('cls')
            game += 1
            if game < 20:
                nogeenkeer = input('Wil je opnieuw?')
                if nogeenkeer == 'nee':
                    print(f'{punten} aantal punten')
                    stop = True
        stoppen = input('Typ quit om vervroegd te stoppen. Als je verder wilt gaan klik enter')

        if stoppen == 'quit':
            print(f'Je bent met {punten} punten geëindigt en na {ronde} ronde(s) gestopt.')
            stop = True

        print(punten)    
print(f'{punten}punten als eindstand')
