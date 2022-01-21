harommaloszthato: int =0


print("Kezdő érték")
kezdoertek: int=int (input())

print("Vég érték")
vegertek: int=int (input())



for i in range(kezdoertek, vegertek +1, 1):
    if  ( i % 2 != 0 and  i % 3 == 0):
            harommaloszthato += 1

print(f"3-al osztható számok száma{harommaloszthato}")
