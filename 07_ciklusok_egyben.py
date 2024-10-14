# sor = 1
# while sor <= 3:
#     oszlop = 1
#     while oszlop <= 7:
#         print('O ', end='')
#         oszlop = oszlop + 1
#     print('')
#     sor = sor + 1

"""
1. Feladat - Pocak
Készíts egy programot, amely a felhasználótól bekér egy páros számot, majd ennek megfelelően
rajzol ki a képernyőre egy pocak szerű alakzatot az alábbiak szerint!
"""

szam = int(input("Adj meg egy páros számot! "))

darab = 1
sor = 1
while sor <= szam / 2:
    oszlop = 1
    while oszlop <= darab:
        print('O ', end='')
        oszlop += 1
    print('')
    darab += 1
    sor += 1

darab = szam / 2
sor = szam / 2
while sor >= 1:
    oszlop = 1
    while oszlop <= darab:
        print('O ', end='')
        oszlop += 1
    print('')
    darab -= 1
    sor -= 1