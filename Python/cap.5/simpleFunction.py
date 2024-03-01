def Sum (X, Y):
    resultSum = X + Y
    return resultSum

objectA = int(input("Type a value to A: "))
objectB = int(input("Type a value to B: "))
objectC = int(input("Type a value to C: "))

firstSum = Sum(objectA, objectB)
print("a + b = %d" % firstSum)

secondSum = Sum(objectB, objectC)
print("b + c = %d" % secondSum)
