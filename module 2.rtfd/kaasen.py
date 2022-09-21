 


geel = input('is de kaas geel?')
if geel == "ja":
    gaten = input("zitten er gaten in de kaas?")
    if gaten == "ja":
        duur = input("is de kaas belachelijk duur?")
        if duur == "ja":
            print("je kaas heet emmentahler")
        elif duur == "nee":
            print("je kaas heet leerdammer")
    elif gaten == "nee":
        steen = input("is de kaas zo hard als steen?")
        if steen == "ja":
            print("je kaas heet parmigiano reggiano")
        elif steen == "nee":
            print("je kaas heet goudse kaas")

elif geel == "nee":
    blauw = input("heeft de kaas blauwe schimmel?")
    if blauw == "ja":
        morst = input("heeft de kaas een korst?")
        if morst == "ja":
            print("je kaas heet Blue de Rockbaron")
        elif morst == "nee":
            print("je kaas heet Foume d Ambert")
    elif blauw == "nee":
        korst = input("heeft de kaas een korst?")
        if korst == "ja":
            print("je kaas heet camembert")
        elif korst == "nee":
            print("je kaas heet mozzarella")