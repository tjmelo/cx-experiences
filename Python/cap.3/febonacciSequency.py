'''
- Febonacci sequency

'''

inputNumber = 0

while inputNumber < 2:
    try:
        inputNumber = int(input("Type a number (> 1): "))

        if inputNumber < 2:
            print("Type number >= 2")

    except:
        print("The typed data should be a interger number.")

    elementA = 0
    elementB = 1

    print("0, 1, ", end="")

    i = 0

    while i < inputNumber - 2:
        elementC = elementA + elementB
        print("%d, " % elementC, end="")

        elementA = elementB
        elementB = elementC

        i += 1

    print("\nEnd of program")
