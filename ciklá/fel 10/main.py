import os
import time

n: int = None
tmp: str = ""
otteloszthatoszamoka: int = 0
tizeneggyelosthatoszamokszama: int = 0

while(n == None):
    tmp = input("Adjon meg egy max 2 jegyü számot ")

    if(tmp.replace("-","").isdigit()):
        if(int(tmp) >= 0 and int(tmp) <= 99):
            n = int(tmp)                
        else:
            print("nem kétjegyű")
    else:
        print("nem szám")
        time.sleep(2)
        os.system("cls")

print("kettővel osztahó számok ")
for j in range(0, n +1, +1):
    if(j % 2 == 0):
        print(f"{j}")
    if(j % 5 == 0):
        otteloszthatoszamoka = otteloszthatoszamoka + j
    if(j % 11 == 0):
        tizeneggyelosthatoszamokszama += 1
print("azon számok amik 7-el osztva 3")
for i in range(0, n +1, +1):
    if(j % 7 == 3):
        print(f"{i}")
print(F"öttel osztható számok száma {otteloszthatoszamoka} és a 11-el oszthatóakké {tizeneggyelosthatoszamokszama}")