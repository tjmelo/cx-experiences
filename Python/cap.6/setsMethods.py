fistSets = {1, 2, 3, 4, 5, 6}

fistSets.add(7)
fistSets.add(8)

secondSets = {2, 4, 6}
secondSets.issubset(fistSets) # true

fistSets.issubset(secondSets)
fistSets.issuperset(secondSets)

thirdSets = fistSets.difference(secondSets) # like a-b
print(thirdSets)

someNumber = 5

fistSets.remove(someNumber)
print(fistSets) 
fistSets.pop()
print(fistSets)

fistSets.isdisjoint(secondSets) # A and B intersection is empty
someList = [5, 9, 'a']
print(fistSets.union(someList))
