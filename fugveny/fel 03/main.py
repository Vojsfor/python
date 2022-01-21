import os
import time
import datetime

nev: str= None
szuletesiev: int= None
felhasznalonev: int = None

#nev bekérése
def nevbeolvasas() -> str:
    while(nev == None):
        data :str=input("kérem a nevét: ")
        if(len(data) > 3):
            nev=data
        else:
            print("Túl rövid")
            time.sleep(2)
            os.system("cls")
#születéséi év
def szuletesievbekerese() -> int:
    eredmeny : int = None
    ma: datetime = datetime.datetime.now()# lekéri a mai évet
    jelenlegiEv: int = int(ma.strtime("%Y")) #viszadja a mai évet

    while(eredmeny == None):
        data: str = input("Kérem a születési évet")
        if(data.replace("-","").replace(".","").isdigit()) 
            eredmeny = int(data)
            if(eredmeny >= jelenlegiEv or eredmeny <= 0):
                eredmeny = None
                print("Nem lehet több mint ma!")
                time.sleep(2)
                os.sytem("cls")
            else:    
                return eredmeny
        else:
            print("Nem szám")
            time.sleep(2)
            os.system("cls")
#életkor számolása
def eletkorszamolasa(ev:int) -> int:
    ma: datetime = datetime.datetime.now()
    jelenlegiEv: int = int(ma.strtime("%Y"))

    return jelenlegiEv - ev

#kiiratás
def kiiras(nev:str, ev: int) -> None
    print(f"{nev} ön az idén {ev} éves")

#főprogram
felhasznalonev = nevbeolvasas()
szuletesiev = szuletesievbekerese()

kor = eletkorszamolasa()

kiiras(felhasznalonev, kor)