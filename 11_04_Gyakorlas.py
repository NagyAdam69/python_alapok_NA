"""1. Egyszerű számbekérő
Kérj be egy számot a felhasználótól, és döntsd el, hogy páros vagy páratlan. Írd ki az eredményt!”””
"""
def elso_feladat():
    szam = int(input("Adj meg egy egész számot: "))
    if szam % 2 == 0:
        print("A szám páros")
    else:
        print("A szám páratlan")

"""
2. Összegszámítás
Kérj be egy egész számot, és számítsd ki az 1-től a megadott számig terjedő egész számok összegét.
"""
def masodik_feladat():
    osszeg = int(input("Adj meg egy egész számot: "))

    for i in range(osszeg):
        osszeg += i
    print(f"Az összeg: {osszeg}")

"""
3. Számok listázása és összegzése
Írj egy programot, amely bekér  n számot a felhasználótól, majd egy while ciklussal megkérdezi a felhasználót, hogy szeretne-e újabb számot megadni.
Addig folytassa a program a számok bekérését, amíg a felhasználó igennel válaszol. A program végén jelenítse meg a bekért számok összegét.
b) jelenítse meg a bekért számokat (lista használata)
"""
def harmadik_feladat():
    osszeg = 0
    while True:
        szam = int(input("Adj meg egy számot: "))
        osszeg += szam
        kerdes = str(input("Elég lesz? (i/n): "))
        if kerdes == "i":
            print(f"A számok összege: {osszeg}")
            break



"""
4. Két szám közötti számok
Kérj be két számot a felhasználótól (a és b). Írasd ki az összes számot a és b között.
b) Ha a nagyobb, mint b, akkor csökkenő sorrendben írasd ki őket.
"""
def negyedik_feladat():
    a = int(input("Adj meg egy számot: "))
    b = int(input("Adj meg még egy számot: "))
    if a < b:
        for i in range(a, b - 1):
            a += 1
            print(a)
    else:
        for i in range(b + 1, a):
            a -= 1
            print(a)

"""
5. Egyszerű jelszókérés
Készíts egy programot, amely egy előre meghatározott jelszót vár el a felhasználótól. A program addig kérdez, 
amíg a helyes jelszót meg nem adják. Ha eltalálja a jelszót, jelenjen meg egy üzenet, hogy „Sikeres belépés”.
"""
def otodik_feladat():
    while True:
        jelszo = input("Adja meg a jelszót: ")
        if jelszo == "kukucs":
            print("Sikeres belépés.")
            break
        else:
            print("Helytelen jelszó.")


"""
6. Szorzótábla
Írasd ki egy adott szám szorzótábláját 1-től 10-ig. Például, ha a felhasználó 5-öt ad meg, akkor az eredmény legyen:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
"""
def hatodik_feladat():
    szam = int(input("Adj meg egy számot: "))
    for i in range(1, 11):
        print(f"{szam} * {i} = {szam * i}")
"""
7. Maximum keresés lista elemeiben
Készíts egy programot, amely bekér 5 számot a felhasználótól, és kiírja a legnagyobb számot. A programban használj egy 
for ciklust a számok bekérésére, és egy if feltételt a legnagyobb szám megkeresésére.
"""


"""
8. Prímszám ellenőrzés
Kérj be egy számot, és döntsd el, hogy prímszám-e vagy sem. A program akkor jelezze, ha prímszámot talált, és akkor is, ha nem az.
"""
def nyolcadik_feladat():
    while True:
        szam = int(input("Adjon meg egy számot: "))
        if szam <= 1:  # 1-nél kisebb szám nem lehet prím
            print("Ez a szám nem prímszám.")
        for i in range(2, int(szam**0.5)+1):
            if szam % i == 0:
                print("Ez a szám nem prímszám.")
            else:
               print("Ez a szám prímszám.")

"""
9. Piramis rajzolása csillagokkal
Kérj be egy számot, amely megadja a piramis magasságát, majd rajzolj ki egy csillagpiramist ennek megfelelően. Például egy 5 magas piramis:
    *
   ***
  *****
 *******
*********

"""
def kilencedik_feladat():
    magassag = int(input("Add meg a piramis magasságát: "))
    for i in range(1, magassag + 1):
        csillagok = '*' * (2 * i - 1)
        print(csillagok.center(2 * magassag - 1))

"""
10. Szorzótábla mátrix formában
Készíts egy programot, amely kiírja az 1-től 10-ig terjedő szorzótáblát egy 10x10-es mátrix formájában. 
Minden sor egy-egy i értéket képviseljen, minden oszlop pedig egy j értéket, és az i * j szorzatot jelenítse meg.
"""
def tizedik_feladat():
    for i in range(1, 11):
        for j in range(1, 11):
                print(f"{i} * {j} = {i * j}" , end="  ")
        print()
