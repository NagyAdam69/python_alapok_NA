"""
szam = int(input("Adj meg egy egész számot:! "))
if szam < 0:
    print("A megadott szám negatív.")
elif szam == 0:
    print("A megadott szám nulla.")
else:
    print("Amegadott szám pozitív.")

print("A program vége.")
"""

# 1.1 Feladat
# Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e!
# A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!

# 1.2 Feladat
# Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó nem a két
# lehetséges válasz (igen/nem) közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"
"""
valasz = str(input("Milyen napod volt? "))
valasz_kisbetu = valasz.lower()

if valasz_kisbetu == "igen":
    print("Ez jó hír!")
elif valasz_kisbetu == "nem":
    print("Az kár...")
else:
    print("Sajnos nem értem a válaszodat! Ne feledd, hogy ez egy eldöntendő kérdés.")

print("A program vége.")
"""

# 2. Feladat
# Készíts egy programot, ami bekér egy számot a felhasználótól, majd kiírja, hogy a megadott szám páros-e vagy páratlan!
#
# [Tipp] A maradékos osztás segít! Mennyivel is kell elosztanod a számot maradékosan, hogy kiderüljön páros-e?
# Ebben az esetben mennyi lesz a maradék?
"""
number = int(input("Írj egy számot: "))

if number % 2 == 0:
    print("Ez a szám páros.")
else:
    print("Ez a szám páratlan.")
"""

# 3. Feladat
# Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban
# tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja,
# hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.

import random
random_number = random.randint(1, 5)
number = int(input("Gondoltam egy számra! "))
print(f"Erre gondoltam: {random_number}")

if random_number == number:
    print("Eltaláltad!")
else:
    print("Nem talált!")