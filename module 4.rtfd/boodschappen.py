boodschappenlijst = {}
x = True

while x == True:
    print('Wat wil jij in je lijst doen?')
    boodschappen_items = input('')
    print('Hoeveel wil jij ervan hebben?')
    boodschappen_aantal = int(input())

    boodschappenlijst.update({boodschappen_items: boodschappen_aantal})
    if boodschappen_items in boodschappenlijst:
        boodschappenlijst[boodschappen_items] += boodschappen_aantal
    quit = input('Typ Stop om te stoppen: ').lower()
    if quit == 'stop':
        x = False

print('- Boodschappenlijst -')
print('')
for item, amount in boodschappenlijst.items():
        print("{}x {}".format(amount, item))
print('')
print('-------------------------------')