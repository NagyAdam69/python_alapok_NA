# import random

# random_szam = random.randint(1, 4)
# print(random_szam)

"""
1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó
által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""
import random

number = int(input("Gondoltam egy számra 1 és 3 között. Próbáld meg kitalálni:\n "))
random_szam = random.randint(1, 3)

if number == random_szam:
    print("Eltaláltad!")
elif number != random_szam:
    print("Nem talált!")
    print(f"A szám {random_szam} volt.")

"""2. Feladat
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a 
választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
"""

print("Fej, vagy írás?")
valasz = input("1: Fej\n2: Írás\nVálasz: ")
fejviras = random.randint(1, 2)

if valasz == fejviras:
    print("Helyes.")
else:
    print("Helytelen.")
