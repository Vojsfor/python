import time
import os
import random

ertek: int = None
szam: int = None

def jatek(szam : int):
    while(tipp != szam):
        tipp: int = tippBeolvasasa()
        if(tipp == szam):
                sikeresTipp(probalkozasokSzama, szam)
            else: 
                sikertelenTipp(tipp, szam)
