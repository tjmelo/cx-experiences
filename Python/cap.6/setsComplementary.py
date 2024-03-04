from random import randint

firstSet = set()

while len(firstSet) < 15:
    firstSet.add(randint(1, 30))

secondSet = set(range(1, 31)) - firstSet

print("Sets A: {}".format(firstSet))
print("Sets B: {}".format(secondSet))
