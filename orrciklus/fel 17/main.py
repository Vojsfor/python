szamok: int = 0
szamokszama: int =0
atlag: float = 0

print("Kezdőérték")
kezdoertek: int = int(input())
print("Végérték")
vegertek: int = int(input())

for i in range(kezdoertek, vegertek +1, 1):
    szamok += i
    szamokszama += 1

atlag  =  szamok / szamokszama

print(f" számok összegének átlaga: {atlag}")