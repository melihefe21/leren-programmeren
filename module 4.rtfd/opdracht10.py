from fruitmand import fruitmand

newlist = sorted(fruitmand, key=lambda d: d['weight'], reverse=True)
for x in newlist:
    print(x['name'])
    print(x['weight'])