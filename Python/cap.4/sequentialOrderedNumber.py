'''
- To generate an list in ascending order...

'''

listNumber = []
inputNumber = int(input("Type a value: "))

while inputNumber != 0:
    elementPoint = 0

    while elementPoint < len(listNumber) and listNumber[elementPoint] < inputNumber:
        elementPoint += 1
    
    listNumber.insert(elementPoint, inputNumber)
    inputNumber = int(input("Type a value: "))

print("Generated list: ", listNumber)
