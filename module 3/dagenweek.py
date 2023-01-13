vraag = input('welke dag is het vandaag?')
week = ['ma','di','wo','do','vr','za','zo']
while vraag != week[0]:
    print(week[0])
    week.pop(0)