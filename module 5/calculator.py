def addition(number1, number2):
  return number1 + number2

def subtraction(number1, number2):
  return number1 - number2

def multiplication(number1, number2):
  return number1 * number2

def division(number1, number2):
  return number1 / number2

def perform_operation(choice, n1, n2=None):
  if choice == 'A':
    result = addition(n1, n2)
  elif choice == 'B':
    result = subtraction(n1, n2)
  elif choice == 'C':
    result = multiplication(n1, n2)
  elif choice == 'D':
    result = division(n1, n2)
  elif choice == 'E':
    result = addition(n1, 1)
  elif choice == 'F':
    result = subtraction(n1, 1)
  elif choice == 'G':
    result = multiplication(n1, 2)
  elif choice == 'H':
    result = division(n1, 2)
  
  return result

def main():
  while True:
    print("Wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren?")
    choice = input()

    if choice in ['A', 'B', 'C', 'D']:
      print("Voer het eerste getal in:")
      n1 = int(input())
      print("Voer het tweede getal in:")
      n2 = int(input())
    else:
      print("Voer het getal in:")
      n1 = int(input())
      n2 = None

    result = perform_operation(choice, n1, n2)
    print(f"De uitkomst is: {result}")

    print(f"Wil je wat met de uitkomst ({result}) doen? A) iets optellen, B) iets aftrekken, C) met iets vermenigvuldigen, D) ergens door delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of I) niets?")
    choice = input()
    if choice == 'I':
      break

    n1 = result

if __name__ == '__main__':
  main()