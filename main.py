print("Mivel végzödjön a számpiramis?")

vegertek = int(input())
szamok: str = ""
if(vegertek == 0):
    print("0")
else:
    for i in range(0, vegertek, 1):
        
        szamok += f"{i + 1} "
        
        print(f"{szamok}")