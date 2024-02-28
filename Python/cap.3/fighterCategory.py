'''
- Sequency of fighter information

'''

try:
    fighterName = str(input("Type a figther name: "))
    fighterWeight = float(input("Type a figther weight: "))

    pityWeight = 65
    lightWeight = 72
    fastLightWeight = 79
    middleMediumWeight = 86
    middleWeight = 93
    heavyWeight = 100

    if fighterWeight < pityWeight:
        fighterCategory = "PITY"

    elif fighterWeight >= pityWeight and fighterWeight < lightWeight:
        fighterCategory = "LIGHT"

    elif fighterWeight >= lightWeight and fighterWeight < fastLightWeight:
        fighterCategory = "FAST LIGHT"

    elif fighterWeight >= fastLightWeight and fighterWeight < middleMediumWeight:
        fighterCategory = "MIDDLE MEDIUM"

    elif fighterWeight >= middleMediumWeight and fighterWeight < middleWeight:
        fighterCategory = "MIDDLE"

    elif fighterWeight >= middleWeight and fighterWeight < heavyWeight:
        fighterCategory = "MIDDLE HEAVY"

    elif fighterWeight >= heavyWeight:
        fighterCategory = "HEAVY"

    print("The fighter {} weight {} and is in {} category.".format(fighterName, fighterWeight, fighterCategory))

except:
    print("Something was wrong =(")
