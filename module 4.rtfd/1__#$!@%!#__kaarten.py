import random

kaarten = ("harten", "klaveren", "schoppen" , "ruiten")
nummer = ("2","3","4","5","6","7","8","9","10","boer","vrouw","heer","aas")
joker = ["joker","joker"]

for i in (kaarten):
    for x in (nummer):
        bijvoegen = i + x
        joker.append(bijvoegen)

random.shuffle(joker)
for x in range(1,8):
    print(f'Kaart {0}: {joker[0]}')
    joker.pop(0)

print(f"kaarten= {len(joker)} {joker}")
