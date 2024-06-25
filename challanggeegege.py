#we schrijfen een functie met de volgende inhoud
#geef een dict met daarin oliebollen en appelbeignets.
# {oliebollen : 1 appelbeinets : 5}

def calc_prijs(lijstjes):
    PRIJS_OLIEBOLLEN = 1.05
    PRIJS_10_OLIEBOLLEN = 7.50
    PRIJS_BEIGNET = 1.5

    oliebol_price = 0

    if lijstjes['oliebol'] == 10:
        oliebol_price = PRIJS_10_OLIEBOLLEN
    elif lijstjes['oliebol'] > 0 and lijstjes['oliebol'] < 10:
        oliebol_price = PRIJS_OLIEBOLLEN * lijstjes['oliebol']

    beignet_price = PRIJS_BEIGNET * lijstjes['appelbeignet']
    
    final_price = oliebol_price + beignet_price

    return final_price

lijstje = {'oliebol': 0, 'appelbeignet': 0}

lijstje['oliebol'] = int(input("Hoeveel oliebollen wilt u? "))
lijstje['appelbeignet'] = int(input("Hoeveel appelbeignets wilt u? "))

total_price = calc_prijs(lijstje)
print(f"De totale prijs is: €{int(total_price)}")