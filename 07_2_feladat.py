# for i in range(5):
#     for j in range(5):
#         print(f"{i}{j}", end=" ")
#     print()

"""2. Feladat - \
Készíts egy programot, amely egymásba ágyazott ciklusok
segítségével rajzolja ki egy 5 x 5-ös mezőben az alábbi alakzatot!

O . . . .
. O . . .
. . O . .
. . . O .
. . . . O"""

# for i in range(5):
#     for j in range(5):
#         if i == j:
#             print("0 ", end=" ")
#         else:
#             print(". ", end=" ")
#     print()

"""3. Feladat - X
Készíts egy programot, amely egymásba ágyazott ciklusok 
segítségével rajzolja ki egy 7 x 7-es mezőben az alábbi alakzatot!

O . . . . . O 
. O . . . O .
. . O . O . .
. . . O . . .
. . O . O . .
. O . . . O .
O . . . . . O"""

for i in range(7):
    for j in range(7):
        if i == j:
            print("0 ", end="")
        elif i + j == 6:
            print("0 ", end="")
        else:
            print(". ", end="")
    print()