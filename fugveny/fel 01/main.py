from mfugvenyek import *
from inputlid import *

osszeg: float = None
kulombseg: float = None
szorzat:  float = None
hanyados: float = None
szam1: float = None
szam2:float = None

szam1 = tizedesszambeolvasas("Kérem az első számot")
szam2 = tizedesszambeolvasas("Kérem az második számot")

osszeg = osszeadas(szam1,szam2)
kulombseg = kivonas(szam1,szam2)
szorzat = szorzas(szam1,szam2)
hanyados = osztas(szam1,szam2)

print(f"a számok összege {osszeg}")
print(f"a számok külömbsége {kulombseg}")
print(f" szorzatuk{szorzat}")
print(f"hányadosuk {hanyados}")
    