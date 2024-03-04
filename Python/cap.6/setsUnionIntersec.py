msgInput = "Type a number: "
firstSets = set()
secondSets = set()

def toIteratesets(sets):
    getInput = int(input(msgInput))
    while getInput != 0:
        sets.add(getInput)
        getInput = int(input(msgInput))

print("First set of data")
toIteratesets(firstSets)

print("Second sets of data")
toIteratesets(secondSets)

print("Sets 1: {}".format(firstSets))
print("Sets 2: {}".format(secondSets))

print("Union of Sets 1 and Sets 2")
print(firstSets | secondSets)

print("Intersection of Sets 1 and Sets 2")
print(firstSets & secondSets)
