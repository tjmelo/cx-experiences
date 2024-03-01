from random import randint

sizeOfList = int(input("Type the size of list: "))
elementList = []
i = 0

while (i < sizeOfList):
    aleatoryNumber = randint(10, 50)
    
    if aleatoryNumber not in elementList:
        elementList.append(aleatoryNumber)
        i+=1
    else:
        continue

print("Generated list: ", elementList)

elementList.sort()
print("Ordered list:", elementList)
