# szam = 1
# while szam <= 10:
#     print(szam)
#     # szam = szam + 1
#     szam += 1


# folytatja = True
# while folytatja:
#   print('Vidd ki a szemetet!')
#   valasz = input('Mondjam még egyszer? (i/n)')
#   if valasz == 'n':
#       folytatja = False
# print('>> Program vége! <<')

"""1. Feladat
Írj egy programot, amely kiírja a páros számokat 1 és 10 között!
"""

# szam = 1
# while szam <= 10:
#     if szam % 2 == 0:
#         print(szam)
#     # szam = szam + 1
#     szam += 1

"""
2. Feladat
Írj egy programot, amely csökkenő sorrendben írja ki a számokat 1 és 10 között!
"""

# szam = 10
# while szam > 0:
#     print(szam)
#     # szam = szam + 1
#     szam -= 1

"""3. Feladat
Írj egy programot, amely kiírja a páratlan számokat csökkenő sorrendben 1 és 10 között!
"""

# szam = 10
# while szam > 0:
#     if szam % 2 != 0:
#         print(szam)
#     # szam = szam + 1
#     szam -= 1

"""
5. Feladat
Írj egy programot, amely a felhasználótól páros számot kér be. Amennyiben a megadott szám páratlan, újra és 
újra megtörténik az adatbekérés mindaddig, amíg végül páros számot nem ad meg a felhasználó.
"""
folytat = True

while folytat == True:
    user_input = int(input("Írj egy páros számot: "))
    if user_input % 2 == 0:
        print("Köszönöm szépen.")
        folytat = False


