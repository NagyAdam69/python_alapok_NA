"""Thonny fejlesztői környezetben készíts egy rövid programot, amely
  -kommentként tartalmazza a program funkciójának leírását,
  -konstansként tárolja PI értékét,
  -egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
  -kiszámolja és a képernyőre kiírja a kör kerületét és területét!"""

# A pi kerekített értéke
PI = 3.14
# A kör sugara
r = 5

# Kerület
kerulet = 2 * r * PI

print(f"A kör kerülete {kerulet} cm nagyságú.")

# Terület
terulet = r * r * PI

print(f"A kör területe {terulet} cm^2 nagyságú.")

# ----------------------------------------------------------------------------

"""Készíts egy rövid programot, amely egy változóban eltárol egy szót. Próbáld meg ennek a változónak a
    tartalmát int értékké átalakítani. Mit tapasztalsz? Milyen üzenet jelenik meg a képernyőn?"""

# allat = int("kutya")

# print(allat)
# ValueError: invalid literal for int() with base 10

# ------------------------------------------------------------------------------

"""Készíts egy rövid programot, amelyben egy olyan változó értékét szeretnéd kiíratni, ami előzőleg nem is
    szerepel a kódodban. Hogyan jelöli a fejlesztői környezet a hibát? Futtasd! Milyen hibaüzenetet kapsz?"""

# print(ember)
# NameError: name 'ember' is not defined