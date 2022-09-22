iphone = int(input('hoe duur is de iphone?'))
samsung = int(input('hoe duur is de samsung?'))


ja = iphone - samsung
if iphone > samsung and ja <= 50:
    print(f'De iphone is het duurst, de telefoon kost: {iphone} euro')
    print(f'De samsung is het goedkoopst,de telefoon kost: {samsung} euro')
    print(f'Het advies is dus de iphone te kopen. Deze is namelijk {iphone - samsung} euro goedkoper/duurder dan de iphone')
if iphone > samsung and ja >= 51:
    print(f'De iphone is het duurst, de telefoon kost: {iphone} euro')
    print(f'De samsung is het goedkoopst,de telefoon kost: {samsung} euro')
    print(f'Het advies is dus de Samsung te kopen. Deze is namelijk {iphone - samsung} euro goedkoper/duurder dan de iphone')
elif samsung > iphone:
    print(f'De samsung is het duurst, de telefoon kost: {samsung} euro')
    print(f'De iphone is het goedkoopst,de telefoon kost: {iphone} euro')
    print(f'Het advies is dus de iphone te kopen. Deze is namelijk {iphone - samsung} euro goedkoper/duurder dan de iphone')
elif iphone == samsung:
    print('ze zijn hetzelfde')














# print(f'De iphone is het duurst, de telefoon kost: {iphone} euro')
# print(f'De samsung is het goedkoopst,de telefoon kost: {samsung} euro')
# print(f'Het advies is dus de Samsung te kopen. Deze is namelijk {iphone - samsung} euro goedkoper/duurder dan de iphone')

# print(f'iphone kost{iphone} euro en de samsung kost{samsung} euro')
# print (f'{iphone - samsung} is het verschil tussen de twee')