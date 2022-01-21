import random
import os
import time

szam: int = random.randint(0,9)
tippeltszam: str = ""
tipp: int = 5

print(" Egy szám 0 és 9 közt")
while( tippeltszam != szam):
    if(tipp <= 0):
        print("nincs több próba")
        time.sleep(2)
        os.system("cls")
        break
    tippeltszam = input("A tipp:")
    
    if(tippeltszam.isdigit()):
        
        if(tippeltszam == szam):
            print(f"Talált, maradt próba {tipp}")
        else:
                  
            print(f"Nem talált, maradt próbák {tipp}")
            tipp -= 1
    else:
        print("Nem számot adott meg")
        time.sleep(2)
        os.system("cls")
