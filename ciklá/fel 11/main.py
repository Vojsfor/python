import os
import time
import random

parosszam: int = None
paratlanszam: int = None
tmp: int = 0
randomszam: int = 0
while(parosszam == None):
    tmp = input("Adjon meg egy paros szamot:")
    if(tmp.replace("-","").isdigit):
        parosszam = int(tmp)
        if(parosszam % 2 == 0):
            tmp = 0
        else:
            print("nem páros")
            time.sleep(2)
            os.system("cls")
            parosszam = None
    else:
        print("nem számot adott meg")
        time.sleep(2)
        os.system("cls")

while(paratlanszam == None):
    tmp = input("Egy páratlanat, de nagyobb legyen")
     if(tmp.replace("-","").isdigit):
        paratlanszam = int(tmp)
        if(paratlanszam % 2 != 0):
            if(paratlanszam > parosszam):
                tmp = 0
            else: 
                print(" nem nagyobb")
                 time.sleep(2)
                os.system("cls")
                paratlanszam = None
        else:
            print("nem páratlan")
            time.sleep(2)
            os.system("cls")
            paratlanszam = None
    else:
        print("nem számot adott meg")
        time.sleep(2)
        os.system("cls")

randomszam = random.randint(parosszam, paratlanszam)

if(abs(paratlanszam - abs(randomszam)) > abs(randomszam - abs(parosszam))):
    print(f"a páratlan számtól messzeb a(z) {randomszam} ")
elif(abs(paratlanszam - abs(randomszam)) = abs(randomszam - abs(parosszam)))
    print(f" a kétszámtól ugyan olyan messze van  a(z) {randomszam}")
else:
    print(f"a páros számtól messzeb a(z) {randomszam}")