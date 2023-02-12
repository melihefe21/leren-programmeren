def fibonacci(x):
    NummerList = [0,1]
    for i in range(0,x):
        NummerList.append(NummerList[-1] + NummerList[-2])
    return NummerList

UserInt = int(input('Hoeveel nummers wil je in de Fibonnaci-Reeks?'))

print(fibonacci(UserInt))