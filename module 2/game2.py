import random

def fight(max_guess: int = 4) -> bool:
    min_guess = 1
    max_guess = 4
    number_to_guess = random.randint(min_guess, max_guess)
    
    while True:
        user_guess = int(input(f"Guess a number between {min_guess} and {max_guess}: "))
        
        if min_guess <= user_guess <= max_guess:
            if user_guess == number_to_guess:
                print("You won!")
                return True
            else:
                print("Try again.")
        else:
            print("Number is out of range. Please guess a number between 1 and 4.")



result = fight()
if result:
    print
else:
    print("jij bent zo slecht! probeer maar opnieuw")