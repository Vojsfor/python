import os
import time

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
