paroSszamokOsszege: int =0

paratlanszamokszorzata: int =1

print("Kezdő érték")
kezdoertek: int=int (input())

print("Vég érték")
vegertek: int=int (input())


for i in range(kezdoertek, vegertek +1, +1 ):
    if  ( i % 2 == 0):
        paroSszamokOsszege += i
    else:
        paratlanszamokszorzata *=i


print(f"a páros számok összege {paroSszamokOsszege}")
print(f"a páratlan számo szorzata {paratlanszamokszorzata}")
