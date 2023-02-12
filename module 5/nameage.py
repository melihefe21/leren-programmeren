def naamleeftijd(x: list):
    naam = input('Geef naam: ').capitalize()
    leeftijd = input('Geef een leeftijd: ')
    NamenEnLeeftijd.append({'naam': naam, 'leeftijd':leeftijd})
    return x

NamenEnLeeftijd = []
getage = True
while getage:
    naamleeftijd(NamenEnLeeftijd)
    stop = input('Toets enter om door te gaan of stop om te printen:').lower()
    if stop == 'stop':
        getage = False      

x = len(NamenEnLeeftijd)
for aantallen in range(0,x):
    print(f'{NamenEnLeeftijd[aantallen]["naam"]} is {NamenEnLeeftijd[aantallen]["leeftijd"]}')