from fruitmand import fruitmand

ding = False
cirkel = 0
nietrond = 0

while not ding:
    kleur = input("Geef een kleur op: ").lower()
    for x in fruitmand:
        if kleur == x['color']:
            if x['round']:
                cirkel += 1
            else:
                nietrond += 1
            ding = True
    if not ding:
        print(f"De kleur {kleur} zit er niet in de fruitmand")

if cirkel > nietrond:
    print(f'Er zijn {cirkel - nietrond} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}')
elif cirkel < nietrond:
        print(f'Er is {abs(cirkel - nietrond)} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur}')
else:
    print(f'Er zijn {cirkel} ronde vruchten en {nietrond} niet ronde vruchten in de kleur {kleur}')