szum: int= 0
szorzat: int= 1

print("Kezdő érték")
kezdoertek: int=int (input())

print("Vég érték")
vegertek: int=int (input())



for i in range(kezdoertek, vegertek +1, +1 ):
    
    szum += i
    szorzat *= i

print(f" a számok összege {szum}, szorzatta {szorzat}")
    
v: str = str(szorzat)

for j in range(0, szorzat , 1)