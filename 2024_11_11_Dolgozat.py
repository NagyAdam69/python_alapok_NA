"""A csoport:
Készítsünk programot, amely dinnyék csomagolásához végez számításokat. A
dinnyéket szalaggal kell átkötni úgy, hogy kétszer körbe érje őket, és a masni
készítéséhez számolunk még 60 cm-t. A program kérje be a dinnye átmérőjét, a
dinnyék számát, és a rendelkezésre álló szalag hosszát! Számítsa ki, és írja a
képernyőre, hogy a bekért számú dinnye csomagolásához hány méter szalagra van
szükség, valamint állapítsa meg, hogy elegendő szalagunk van-e a művelet
elvégzéséhez, és ezt is közölje a felhasználóval!"""

pi = 3.14
atmero = float(input("Adja meg a dinnye átmérőjét (cm): "))
darab = int(input("Ajda meg a dinnyék számát: "))
hossz = float(input("Adja meg a rendelkezésre álló szalag hosszát (cm): "))

per_dinnye = atmero * pi * 2 + 60
osszes_dinnye = per_dinnye * darab

print() # sor törés

print(f"Ennyi dinnye becsomagolásához {osszes_dinnye / 100} méter szalagra van szükség.")
print(f"Randelkezésre álló szalag hossza: {hossz / 100} méter.")

if hossz < osszes_dinnye:
    print("A rendelkezésre álló szalag NEM ELÉG hosszú az összes dinnye csomagolásához.")
else:
    print("A rendelkezésre álló szalag ELÉG hosszú az összes dinnye csomagolásához.")

