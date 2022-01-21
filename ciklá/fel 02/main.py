# nem üres
#nem szóköz
# több mint 3
import os
import time
nev: str = ""


while(nev == "" or nev.isspace() or len(nev) < 3):
    print("név")
    nev = input()
        
    if(nev == ""):
        print("nem adott meg semmit!")
        time.sleep(2)
        os.system("cls")
            
    elif(nev.isspace()):
        print("csak space nem jó")
        time.sleep(2)
        os.system("cls")
        
    elif(len(nev) < 3):
        print("túl rövid")
        time.sleep(2)
        os.system("cls")
        
print(f" Üdvözlöm {nev}")