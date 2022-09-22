naam = input('hoe heet u?') .lower()
gender = input ('ben je een man of een vrouw?')
haren = int(input('hoelang zijn uw krullen'))
snor = int(input("hoe breed is uw snor in cm?"))
dieren = int(input('hoeveel jaar praktijervaring heeft u met dieren-dressuur?'))
jongleren = int(input('hoeveeljaar ervaring met jongleren heeft u?'))
acrobatiek = int(input('hoeveel jaar ervaring heeft u voor praktijk ervaring met acrobatiek?'))
rijbewijs = (input('heeft u een geldig vrachtwagen bewijs?'))
hoed = input('heeft u een hoge hoed?')
diploma = int(input("welk mbo niveau diploma heeft u je?"))
lengte = int(input('hoelang bent u in cm?'))
zwaar = int(input('hoeveel weegt u in kg?'))
certificaat = input('heeft u de Overleven met gevaarlijk personeel certificaat?')
leeftijd = int(input('hoe oud bent u?'))
hoelang = int(input('hoelang heeft u op school gezeten?'))
wat = input('wat bent u (mens, dier, alien...?')





if dieren >= 4 or jongleren >= 5 or acrobatiek >= 4 and rijbewijs == 'ja' and hoed == 'ja' and diploma >= 4 or (gender == 'man' and snor == 'ja') or (gender == 'vrouw' and haren >=20) and lengte >=150 and lengte <= 220 and zwaar >= 90 and zwaar <= 120 and certificaat == 'ja' and leeftijd >= 18 and hoelang >= 12 and wat == 'mens':
    print('je bent geslaagd!!')


else:
    print('je bent niet geslaagd')






# if gender == 'vrouw' or haren >= 20 or dieren >= 4 or jongleren >= 5 or acrobatiek >= 3 or rijbewijs == 'ja' or hoed == 'ja' or diploma >= 4 or lengte >= 150 and lengte <= 220 or zwaar >= 90 and zwaar <= 120 or certificaat == 'ja' or leeftijd >= 18 or hoelang >= 12 or wat == 'mens':
#     print('u bent geslaagd u kunt morgen komen werken!!')

# elif gender == 'man' and snor >= 10 and dieren >= 4 or jongleren >= 5 or acrobatiek >= 3 or rijbewijs == 'ja' or hoed == 'ja' or diploma >= 4 or lengte >= 150 and lengte <= 220 or zwaar >= 90 and zwaar <= 120 or certificaat == 'ja' or leeftijd >= 18 or hoelang >= 12 or wat == 'mens':
#     print('u bent geslaagd u kunt morgen komen werken!!')

# naam = input('hoe heet u?') .lower()
# gender = input ('ben je een man of een vrouw?')
# if gender == "man":
#     if snor < 9: 
#         print('je mag niet verder gaan met solliciteren')
#     elif snor >= 10:
#         if dieren <= 3:
#             print('je mag niet verder gaan met solliciteren')
#         elif dieren >= 4:
#             if jongleren <= 3:
#                 print('je mag niet verder gaan met solliciteren')
#             elif jongleren >= 4:
#                 if acrobatiek <= 2:
#                     print('je mag niet verder gaan met solliciteren')
#                 elif acrobatiek >= 3:
#                     if rijbewijs == 'nee':
#                         print('je mag niet verder gaan met solliciteren')
#                     elif rijbewijs == 'ja':
#                         if hoed == 'nee':
#                             print('je mag niet verder gaan met solliciteren')
#                         elif hoed == 'ja':
#                             if diploma <= 3:
#                                 print('je mag niet verder gaan met solliciteren')
#                             elif diploma >= 4:
#                                 if lengte <= 149:
#                                      print('je mag niet verder gaan met solliciteren')
#                                 elif lengte >= 150:
#                                     if zwaar <= 89:
#                                         print('je mag niet verder gaan met solliciteren')
#                                     elif zwaar >= 90:
#                                         if certificaat == 'nee':
#                                             print('je mag niet verder gaan met solliciteren')
#                                         elif certificaat == 'ja':
#                                             if leeftijd <= 17:
#                                                 print('je mag niet verder gaan met solliciteren')
#                                             elif leeftijd >= 18:

# elif gender == "vrouw":
#     haren = int(input('hoelang zijn uw krullen'))
#     if haren <= 19:
#         print('je mag niet verder solliciteren')
#     elif haren >= 20:
#         if dieren <= 3:
#             print('je mag niet verder gaan met solliciteren')
#         elif dieren >= 4:
#             if jongleren <= 3:
#                 print('je mag niet verder gaan met solliciteren')
#             elif jongleren >= 4:
#                 if acrobatiek <= 2:
#                     print('je mag niet verder gaan met solliciteren')
#                 elif acrobatiek >= 3:
#                     if rijbewijs == 'nee':
#                         print('je mag niet verder gaan met solliciteren')
#                     elif rijbewijs == 'ja':
#                         if hoed == 'nee':
#                             print('je mag niet verder gaan met solliciteren')
#                         elif hoed == 'ja':
#                             if diploma <= 3:
#                                 print('je mag niet verder gaan met solliciteren')
#                             elif diploma >= 4:
#                                 if lengte <= 149:
#                                      print('je mag niet verder gaan met solliciteren')
#                                 elif lengte >= 150:
#                                     if zwaar <= 89:
#                                         print('je mag niet verder gaan met solliciteren')
#                                     elif zwaar >= 90:
#                                         if certificaat == 'nee':
#                                             print('je mag niet verder gaan met solliciteren')
#                                         elif certificaat == 'ja':
#                                             if leeftijd <= 17:
#                                                 print('je mag niet verder gaan met solliciteren')
#                                             elif leeftijd >= 18:




# hoeveel = int(input('hoeveel jaar praktijervaring heeft u met dieren-dressuur?'))
# jongleren = int(input('hoeveeljaar ervaring met jongleren heeft u?'))
# acrobatiek = int(input('hoeveel jaar ervaring heeft u voor praktijk ervaring met acrobatiek?'))


# if hoeveel >= 4:
    