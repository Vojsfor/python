parosSzamok: int =0

paratlanSzamok: int =0

print("Kezdő érték")
kezdoertek: int=int (input())

print("Vég érték")
vegertek: int=int (input())



for i in range(kezdoertek, vegertek +1, 1):
    if ( i % 5 == 0):
        parosSzamok += i
    if (i % 7 == 0):
        paratlanSzamok += i

if (paratlanSzamok > parosSzamok):
    print(f"az 5-el osztható számok száma nagyobb mint a 7-el oszthatóké")
elif (parosSzamok > paratlanSzamok):
    print(f" a 7-el osztható számok száma nagyobb mint a 5-el oszthatóké")
else:
    print(f"mind az 5-el osztható mind a 7-el osztható számok ugyan annyiak")

