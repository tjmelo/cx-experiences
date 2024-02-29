inputThreeNumerals = input("Type three groups of numerals, with space among us: ")

isSplitInput = inputThreeNumerals.split(" ")
print("List of numerals: ", isSplitInput)

group1 = int(isSplitInput[0])
group2 = int(isSplitInput[1])
group3 = int(isSplitInput[2])

print("Group1 = {}, Group2 = {}, Group3 = {}".format(group1, group2, group3))
