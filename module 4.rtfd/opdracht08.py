from fruitmand import fruitmand
fruitmand.append({'name': 'watermeloen', 'weight': 0 , 'round': True})
print(sum(x['weight']for x in fruitmand))