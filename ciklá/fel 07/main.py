import os
import time

kezdoertek: int = None
vegertek: int = None
leptetoszam: int = None
minusz: int = -1
print("Adjon meg egy számot")
kezdoertek = input("")
while(kezdoertek != None):
    if(kezdoertek.replace("-","").isdigit):
        kezdoertek = int(kezdoertek)
        break
    else:
        print("nem számot adott meg")
        time.sleep(2)
        os.sytem("cls")

print("Adjon meg még egy számot, de legyen nagyobb az előzőnél")
vegertek = input("")
while(vegertek != None):
    if(vegertek.replace("-","").isdigit):
        vegertek = int(vegertek)
        break
    else:
        print("nem számot adott meg")
        time.sleep(2)
        os.sytem("cls")
print("Adja meg mennyivel csokennyen a szám, és legyen kisseb a két szám különbségénél")
leptetoszam = input("")
while(leptetoszam != None):
    if(leptetoszam.replace("-","").isdigit):
        leptetoszam = int(leptetoszam)
        if(leptetoszam < vegertek - kezdoertek):
            for j in range(vegertek, kezdoertek, leptetoszam*minusz):
                print(f"{j}")
            break
        else:
            print("Nem kisseb a különbségeknél")
            time.sleep(2)
            os.sytem("cls")

    else:
        print("nem számot adott meg")
        time.sleep(2)
        os.sytem("cls")
