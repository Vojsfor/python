print("X")
x: int= int(input())

if (x >= 100 and x <= 999 ):
    print("100 és 999 között van")
elif (x >= 10 and x <= 99 ):
    print("10 és 99 között van")
elif (x >= 0 and x <= 9 ):
    print("0 és 9 között van")
else:
    print(" se 999 és 100, se 10 és 99, se 0 és 9 között nincs")