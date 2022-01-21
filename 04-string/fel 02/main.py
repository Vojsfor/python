from typing import*

text: str ="bonjur le mode"
textAsList:List[str] = text.split()

print(textAsList)


text ="Katarnya Sfocki Dolata; 190;center"
textAsList = text.split(";")

print(textAsList)


text ="Katarnya Sfocki Dolata; 190;center"

index: int = text.find("at")
indexRight: int =text.rfind("at")

print(index)
print(indexRight)

text ="Katarnya Sfocki Dolata; 190;center"
count: int = text.count("on")

print(count)

text ="Katarnya Sfocki Dolata; 190;center"
text =text.replace("at", "AT")

print(text)