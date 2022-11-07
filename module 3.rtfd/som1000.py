x = 50
y = 50
z = '50'
while y <= 1000:
    x += 1
    y += x
    z += f'+ {x}'
    print(f'{z} = {y}')

