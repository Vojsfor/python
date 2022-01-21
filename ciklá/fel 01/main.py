#pip3 install keyboard

#csomag importálás
import os
#import keyboard
import time

#változók
#nincs értéke, a változás követéséhez, addig fut amíg nincs értéke
number: int= None
#segéd változó 
data: str = ""

while(number == None):
    #beolvasás a konzolról
    data = input("Kerem a szamot: ")
    #a belvasott érték számá alakítható-e?(hogy int vagy float az mindegy)
    #isdigit() bool változót ad
    if(data.isdigit()):
        #ha igaz akkor bisztos számot tudunk belöle csinálni
        number = int(data)
        

    #ha hamis akkor fut le, tehát nincs szám, és a number None marad
    else:
        print("\nNem szamot adott meg!")
        # 3 másodperc = 3000
        time.sleep(3)
        os.system("cls")
        #képernyő törlés
        #print("\nA folytatashoz nyomja meg az Enter gombot")
        # végtelen while, amíg a játékos nem csinál semmit
        #while(True):
        # a játékoss lenyomta az enetert?
        #    if (keyboard.is_pressed('enter')):
        #        os.system("cls")
        #       break
                #megszakítás
print(f" A beolvasott szám {number}")