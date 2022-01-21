import os
import time

valasztas: int = None
print("Válassza ki a kért italt 1 = Cola, 2 = Narcslé, 3 = Redbull, 4 = Kávé ")

while( valasztas == None):
    valasztas = input("")
    if(valasztas.replace("-","").isdigit):
        valasztas = int(valasztas)
        if(valasztas == 1):
            print("Az ital")
        elif(valasztas == 2):
            print("Az ital")
        elif(valasztas == 3):
            print("Az ital")
        elif(valasztas == 5):
            print("Az ital")
        else: 
            print("ilyen ital nincs")
            time.sleep(2)
            os.system("cls")
            valasztas = None
    else:
        print("Nem szám")
        time.sleep(2)
        os.system("cls")