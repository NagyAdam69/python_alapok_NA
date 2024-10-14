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
def main():
    szam = int(input("Adj meg egy páros számot! "))

    if szam % 2 == 0:
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
    else:
        print(f"Kérlek párosat! A {szam} nem páros.")
        main()

main()