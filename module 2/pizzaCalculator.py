# melihefe Erdogan Pizza calculator

import sys
try:
    small_pizza = int(input('hoeveel (25 cm) (7$) small pizzas wilt u?'))
except ValueError:
    print("u heeft iets verkeerd ingevuld, start het programma even opnieuw op en probeer nogmaals.")
    exit()
try:
    medium_pizza = int(input('hoeveel (29 cm) (9.50) medium pizzas wilt u?'))
except ValueError:
    print("u heeft iets verkeerd ingevuld, start het programma even opnieuw op en probeer nogmaals.")
    exit()
try:
    large_pizza = int(input('hoeveel (35 cm) (12$) large pizzas wilt u?'))
except ValueError:
    print("u heeft iets verkeerd ingevuld, start het programma even opnieuw op en probeer nogmaals.")
    exit()
small = 7
medium = 9.50
large = 12
s = small_pizza * small
m = medium_pizza * medium
l = large_pizza * large

print ('-------------------------')
print (f'   {s} voor small')
print (f'   {m} voor medium')
print (f'   {l} voor large')
print (f'   {s + m + l} euro totaal')
print ('-------------------------')





#too easyy
