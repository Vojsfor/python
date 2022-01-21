import os
import time

number: int= None
oszeg: int = 0
proba: int = 0
szamhatar: int= 0
print("adjon megy esgy számot, min 100")
while(szamhatar == 0):
   
    szamhatar = input("Kerem a szamot: ")
    if(szamhatar.replace("-", "").isdigit()):
        szamhatar = int(hatar)
        if(szamhatar < 100):
            print("nem 100 alati")

            time.sleep(2)
            os.system("cls")
    else:
        print("Nem szamot adott meg!")
       
        time.sleep(2)
        os.system("cls")
print("A számok összege több mint  a megadott számé legyen")
while(oszeg < szamhatar):
    
    number = input("Kerem a szamot: ")
    
    if(number.replace("-", "").isdigit()):
       
        oszeg = oszeg + int(number)
        proba =  proba + 1 
        print(f"próbák száma {proba} a számok összege {oszeg}")
    else:
        print("Nem szamot adott meg!")
       
        time.sleep(2)
        os.system("cls")
       
print(f" a számok összege {oszeg} és a próbák száma {proba}")
