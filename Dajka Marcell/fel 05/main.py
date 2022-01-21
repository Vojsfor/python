print("x")
x: int = int (input())

if (x % 2 == 0):
    if (x % 5 ==  0):
        print("páros és osztható 5-el")
    else:
        print("páros, és nem osztható 5-el")
if (x <= 0):
    if (x <= -100):
        print("az x több mint kétjegyű és minusz")
    elif ( x <= -10):
        print(" az x két jegyű, és negatív ")
    else: 
        print("az szám negatív és egyjegyű")
else: 
    print(" a szám páratlan és pozitív" )