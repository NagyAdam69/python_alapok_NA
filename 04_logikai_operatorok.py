# Összehasonlító operátorok
# ==	egyenlő
# !=	nem egyenlő
# <	    kisebb
# >	    nagyobb
# <=	kisebb vagy egyenlő
# >=	nagyobb vagy egyenlő

# x = 5
# y = -3

# if x < 0 and y < 0:
#     print('mindkettő negatív')

# if x < 0 or y < 0:
#     print('van köztük negatív')

# if not x <= 0:
#     print('x pozitív')


"""1. Feladat
Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót.
"""

# x = int(input("Adj meg egy egész számot: "))
#
# if x % 2 == 0 and x > 0:
#     print("A szám páros és negatív.")
#
# elif x % 2 != 0 and x < 0:
#     print("A szám negatív páratlan")


"""2. Feladat
Készíts egy programot, amely a felhasználótól két külön kérdésben megkérdezi, hogy az ikrek (Henrik és Hanna) jönnek-e 
ma kosrazni! Például így: Jön Henrik ma kosarazni? (igen/nem). A program írja ki, hogy melyik állítás igaz az alábbiak közül:
- egyikük sem jön kosarazni,
- mind a ketten jönnek kosarazni,
- csak az egyikük jön kosarazni.
"""

# henrik = int(input("Henrik jön ma kosarazni?\n1: Igen\n2: Nem\nVálaszod:"))
# hanna = int(input("Hanna jön ma kosarazni?\n1: Igen\n2: Nem\nVálaszod:"))
#
# if henrik == 2 and hanna == 2:
#     print("Egyikük sem jön kosarazni.")
# elif henrik == 1 and hanna == 1:
#     print("Mind a ketten jönnek kosarazni.")
# elif henrik or hanna == 1:
#     print("Csak az egyikük jön kosarazni.")
# else:
#     print("Kérlek a megadott válaszok közül válassz.")

"""3. Feladat
Készíts egy programot, amely a felhasználó által megadott egész számról eldönti, hogy
- csak 3-mal osztható,
- csak 4-gyel osztható,
- 3-mal és 4-gyel is osztható,
- sem 3-mal, sem 4-gyel nem osztható!
"""

number = int(input("Adj meg egy egész számot: "))

if number % 3 == 0 and number % 4 != 0:
    print("A szám csak 3-mal oszható.")
elif number % 4 == 0 and number % 3 != 0:
    print("A szám csak 4-gyel oszható.")
elif number % 3 == 0 and number % 4 == 0:
    print("A szám 3-mal és 4-gyel is oszható.")
elif number % 3 != 0 and number % 4 != 0:
    print("A szám sem 3-mal, sem 4-gyel nem oszható")