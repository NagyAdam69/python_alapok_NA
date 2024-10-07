"""1. Feladat:
    Thonny fejlesztői környezetben készíts egy rövid programot, amely a felhasználótól
   bekéri a kör sugarát, és ennek alapján kiszámolja a kör kerületét és területét!"""

PI = 3.14

r = float(input("A kör sugara: "))

# Kerület
kerulet = 2 * r * PI

print(f"A kör kerülete {kerulet} cm nagyságú.")

# Terület
terulet = r * r * PI

print(f"A kör területe {terulet} cm^2 nagyságú.")

"""2. Feladat: 
    Írj egy programot, ami a felhasználótól bekéri először a keresztnevét, majd a vezetéknevét. A program 
   ezután összefűzi ezeket egy teljes_nev nevű változóba. Végül a program a teljes nevén üdvözli a felhasználót!"""

vezetekn = str(input("A vezeték neved: "))
keresztn = str(input("A kereszt neved: "))
teljesn = vezetekn + " " + keresztn
print(f"A teljes neved: {teljesn}")

"""3. Feladat: 
    Írj egy programot, ami bekér egy számot a felhasználótól, és valamilyen 
   matemataikai sorozataként generál és kiír a felhasználónak egy szerencseszámot!"""

szam = int(input("Véletlen szerű szám: "))
szerencseszam = (szam + 3) * 2 - 7
print(f"A te szerencseszámod a {szerencseszam}")