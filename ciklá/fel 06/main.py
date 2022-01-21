import os
import time

eletkor: int = 0
borszin: int = 0

while(eletkor == 0 and borszin == 1):
    eletkor = input("")
    if(eletkor.replace("-","").isdigit()):
        eletkor = int(eletkor)
        if(eletkor <= 6):
            print(" 0-6 gyerek")
            break
        elif(eletkor <= 18):
            print(" 7-18 iskolás")
        elif(eletkor < 65):
            print(" 19-65 dolgozó")
        elif(eletkor >= 65):
            print("  65- nyugdíjas")
    else:
        print("nem számot adott meg")
        time.sleep(2)
        os.system("cls")

