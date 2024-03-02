def PairOdd(number):
    '''
    - Returns if parameters is pair or odd

    '''
    if number % 2 == 0:
        return "It's pair"
    else:
        return "It's odd"


try:
    inputNumber = int(input("Type a number: "))
    print(PairOdd(inputNumber))
except:
    print("It's not a number!")
