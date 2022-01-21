import os
import time

money: float = None
tmp: str = ""
month: int = 0

while(money == None):
    print("Mennyi megtakarítása van (min 10.000 max 50.000)")
    tmp = (input(""))
    if(tmp.isdigit):
            money = float(tmp)
            if(money < 10000 or money > 50000):
                print("túl kevés/sok")
                time.sleep(2)
                os.system("cls")
                money = None        
    else:
        print(" Nem szám")
        time.sleep(2)
        os.system("cls")

while(money <= 100000):
    money= money * 1.02
    month += 1

print(f"{month} hónap alalatt ériel")