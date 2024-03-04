listNumbers = []
inputNumber = float(input("Type a float number: "))
pathOfFile = './cap.7/files/RealList.txt'

while inputNumber != 0:
    listNumbers.append("{:.3f}\n".format(inputNumber))
    inputNumber = float(input("Type a float number: "))

realNumberFile = open(pathOfFile, 'w')
realNumberFile.writelines(listNumbers)
realNumberFile.close()
