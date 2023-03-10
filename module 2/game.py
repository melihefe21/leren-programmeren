import random
import time
score = 0
loop = True
if loop == True:
        
    def fight(i: int):
        x = random.randint(1, 4)
        if 0 < i < 5:
            if i == x:
                print("You died")
                exit()
            else:
                print("You won!")
        else:
            print("Number is too big/small")
            print("Game over...")
            exit()

    def escape(i: int): 
        x = random.randint(1, 2)
        if 0 < i < 3:
            if i == x:
                print("You died")
                exit()
            else:
                print("You successfully escaped")
        else:
            print("Number is too big/small")
            print("Game over...")
            exit()

    def fighting(i: str):
        if i == "FIGHT":
            if weapon == "N":
                print("You lost because you didnt have a sword...")
                exit()
            else:
                usernumber = int(input("Enter a number between 1-4: "))
                fight(usernumber)
        elif i == "RUN":
            usernumber = int(input("Enter 1 or 2: "))
            escape(usernumber)
        else:
            print("Invalid answer... Game over")
            exit()

    def bossFight(i: int):
        counter = random.randint(1, 5)
        if 0 < i < 6:
            if counter == i:
                print("You died")
                exit()
        else:
            print("hit")

    def printDelay(t: str, d=0.75):
        time.sleep(d)
        print(t)
    printDelay("You wake up in a house...")
    printDelay("npc: 'Hey you, you're finally awake.'")
    printDelay("npc: 'What is your name if i may ask?'")
    name = input("Input username: ")
    print(f"npc: 'Hello '{name}' it's nice to meet you.'")
    time.sleep(1)
    help = input("npc: There is a boss near the village will you help us kill it?' (YES/NO): ").upper()
    if help == "YES":
        printDelay("npc: 'Thank you so much, you are a true hero.'")
    elif help == "NO":
        print("The village later got destroyed by the boss.")
        print("game over")
        exit()
    else:
        print("invalid answer... Game over")
        exit()
    time.sleep(1)
    weapon = input("You first need a weapon , do you want me to give a sword? (YES/NO): ").upper()
    if weapon == "N0":
        weaponSure = input("Are you sure you dont want a sword? (YES/NO): ").upper()
        if weaponSure == "YES":
            printDelay("Okay... The choice was yours")
        elif weaponSure == "NO":
            printDelay("Take good care of the sword")
            weapon = "YES"
    elif weapon == "YES":
        printDelay("Take good care of the sword")
    else:
        print("Invalid answer... Game over")
        exit()
    boss = input("Do you first want to train or immediately fight the boss? (Train/Fight): ").upper()
    if boss == "FIGHT":
        printDelay("You tried fighting the boss but sadly failed...")
        printDelay("To fight the boss you  need a killer sword!")
        exit()
    elif boss == "TRAIN":
        printDelay("Good, you shall now go to the forest and start your training")
        printDelay("You start wandering through the forest")
    else:
        print("invalid answer... Game over")
        exit()
    time.sleep(1)
    print("You encountered a goblin!")
    fightRun = input("Do you want to fight it or run away? (Fight/Run): ").upper()
    fighting(fightRun)
    printDelay("You continue wandering in the forest...")
    printDelay("You encounter a skeleton wielding a strange sword")
    fightRun = input("Do you want to fight it or run away? (Fight/Run): ").upper()
    if fightRun == "FIGHT":
        killerSword = True
    else:
        killerSword = False
    fighting(fightRun)
    printDelay("You are now going to fight the boss!")
    if not killerSword:
        print("You died because you didnt have the killer sword...")
        exit()
    else:
        userNumber = int(input("Enter a number between 1-5"))
        bossFight(userNumber)
        userNumber = int(input("Enter a number between 1-5"))
        bossFight(userNumber)
        userNumber = int(input("Enter a number between 1-5"))
        bossFight(userNumber)
    print(f"Congrats '{name}'! you saved the village and you are their saviour!")
    score += 1

stop =  input("click enter if you wanna continue. Type 'stop'if you wanna stop")
if stop == "stop":
    loop = False
    print(f'your score was {score}')
