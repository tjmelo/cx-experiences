'''
### TOTALIZER PROGRAM ###

- Get a quantity of number to be generated by system
- Iterate by sequencial number and amount of total generated numbers

'''

from random import randint

integerNumber = int(input("Type a numeral: "))
totalAmount = 0
i = 1

while i<= integerNumber:
    aleatoryNumeber = randint(1, 50)
    print("Generated {} value = {}".format(i, aleatoryNumeber))
    totalAmount += aleatoryNumeber
    i += 1

print("\n Amount of generated values = %d" % totalAmount)