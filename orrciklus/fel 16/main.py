paratlanszamok: int = 0
parosszamok: int =0

atlag: float = 0
print("Kezdőérték")
kezdoertek: int = int(input())

print("Végérték")
vegertek: int = int(input())

for i in range(kezdoertek, vegertek +1, 1):
    if (i % 2 == 0):
        parosszamok += i
    else:
        paratlanszamok += i

atlag  = (paratlanszamok + parosszamok) / 2

print(f"a páros és a páratlan számok összegének átlaga: {atlag}")