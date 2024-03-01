inputData = input("Type a something numeric: ")

if inputData.isnumeric():
    inputDataToNumber = int(inputData)
    print("The number typed was: {}".format(inputDataToNumber))
else:
    print("Error: Type only numeric data")
