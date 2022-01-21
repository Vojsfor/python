osszeg: int = 0
elojel: int = 1

print("Kezdőérték")
kezdoertek: int = int(input())
print("Végérték")
vegertek: int = int(input())

for i in range(kezdoertek, vegertek +1, 1):
    osszeg += i * elojel
    elojel = elojel * (-1)

print(f" {osszeg}")

bármi ötlet hogy a faszba fogjuk megoldani?