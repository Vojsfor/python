import os
import time

def tizedesszambeolvasas(szoveg:str) -> float:
    szam:float = None
    tmp: str = ""

    while(szam == None):
        tmp = input(szoveg)

        if(tmp.replace("-","",).replace(".","").isdigit()):
            szam= float(tmp)
        else:
            print("Nem szám")
        time.sleep(2)
        os.system("cls")
    return szam

    def egeszszambeolvasas(szoveg:str) -> int:
    szam:int = None
    tmp: str = ""

    while(szam == None):
        tmp = input(szoveg)

        if(tmp.replace("-","",).replace(".","").isdigit()):
            szam= int(tmp)
        else:
            print("Nem szám")
        time.sleep(2)
        os.system("cls")
    return szam

def nevbekeres() -> srt:
    nev: str = None

    while(nev == None):
        data: str = input("Kérem a nevét: ")
        
        if(len(data) < 3):
            print("Túl rövid a név, min 3 karakter")
            time.sleep(2)
            os.system("cls")
        else:
          nev = data

    return nev

def udvozles(nev: str) ->None:
    print(f"Üdvözlöm {nev}!")
