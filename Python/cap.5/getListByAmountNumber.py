'''
- Get a list of integer numebers
- Get a value of reference
- Return how many times this value has shown in list

'''

def HowManyTimesNumberShown(listNumber, refNumber):
    '''
    - Returns how many times the param value has shown in list number

    '''
    counterNumberRef = 0

    for number in listNumber:
        if number ==  refNumber:
            counterNumberRef += 1

    print("{} has shown in the list {} times.".format(refNumber, counterNumberRef))

getListNumber = [20, 15, 23, 20, 65, 47, 8, 5, 6, 15, 24, 14, 12, 54, 56, 24]

try:
    getInputNumber = int(input("Type a number: "))
    HowManyTimesNumberShown(getListNumber, getInputNumber)
except:
    print("It's not a number")

