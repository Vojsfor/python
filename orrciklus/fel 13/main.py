parosSzamok: int =0

paratlanSzamok: int =0

print("Kezdő érték")
kezdoertek: int=int (input())

print("Vég érték")
vegertek: int=int (input())


for i in range(kezdoertek, vegertek +1, 1):
    if  ( i % 2 == 0):
        parosSzamok += i
    else:
        paratlanSzamok += i

if (paratlanSzamok > parosSzamok):
    print(f"a páratlan számok száma nagyobb mint a párosaké")
elif (parosSzamok > paratlanSzamok):
    print(f" a páros számok száma nagyobb mint a páratlanoké")
else:
    print(f"mind a páros és a páratlan számok ugyan annyiak")
