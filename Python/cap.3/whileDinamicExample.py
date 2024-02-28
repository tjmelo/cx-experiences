'''
- Get value of a user's input
- Stay in loop when the value X is diferent of 0
- Get the total of all typed values
- Get how many values were typed

'''

totalOfTypedValues = 0
totalAmountOfValue = 0
valueX = int(input("Type any numeric value: "))

while valueX != 0:
    totalOfTypedValues += 1
    totalAmountOfValue += valueX
    valueX = int(input("Type any numeric value: "))

print('Total of typed values: %d' % totalOfTypedValues)
print('Total of amounted values %d' % totalAmountOfValue)
