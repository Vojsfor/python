import os
import time

szam: int = 0
tmp: str = ""



while(szam < 100 or szam > 999):
    tmp = input("Adjon meg egy 3 jegyű számot")
    if(tmp.replace("-","").isdigit):
        szam = int(tmp)
        if(szam <= 999 and szam >= 100):
            if(szam % 7 == 0):
                print("a szám osztható 7-el")
            else:
                print("a szám nem osztható 7-el")
        else:
            print("Nem három jegyű")
            time.sleep(2)
            os.system("cls")
            szam = 0
         
    else:
        print("Nem számot adott meg")
        time.sleep(2)
        os.system("cls")
        szam = 0
     