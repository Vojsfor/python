print("Kezdő érték")
kezdoertek: int=int (input())

print("Vég érték")
vegertek: int=int (input())

if (kezdoertek % 2 == 0):
    kezdoertek += 1

for i in range(kezdoertek, vegertek, +2 ):
    print(i)