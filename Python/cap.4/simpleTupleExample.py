emptyTuple = () 

print(emptyTuple)
print(len(emptyTuple))

simpleTuple = 3, 6, 9
print(simpleTuple)

diverseTuple = (17, 3, 'txt', 3.8)
print(type(diverseTuple))
print(len(diverseTuple))
print(diverseTuple[0])

diverseTuple = diverseTuple + (15, 16) # concatenation tuple
print(diverseTuple)

multiplyingPrintTuple = (0 ,1)
multiplyingPrintTuple = multiplyingPrintTuple * 6
print(multiplyingPrintTuple)
