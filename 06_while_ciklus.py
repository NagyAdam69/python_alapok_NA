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
import random

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

# folytat = True
#
# while folytat == True:
#     user_input = int(input("Írj egy páros számot: "))
#     if user_input % 2 == 0:
#         print("Köszönöm szépen.")
#         folytat = False

"""6. Feladat
Írj egy programot, amely [1;12] intervallumon állít elő 20 darab véletlenszámot! A képernyőre kizárólag csak 
a 3-mal oszthatóakat írja ki, és a végén informálja a felhasználót arról is, hány darab ilyen szám volt.
"""

osszes_szam = 0
oszthato_harom = 0

while osszes_szam < 20:
    szam = random.randint(1, 12)
    osszes_szam += 1
    if szam % 3 == 0:
        oszthato_harom += 1
        print(szam)

print(f"\nA 12-ből, {oszthato_harom} szám osztható 3-mal.")
