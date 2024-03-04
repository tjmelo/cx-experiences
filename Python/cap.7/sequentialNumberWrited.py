pathOfFile = './cap.7/files/RealNumbers.txt'

realNumberFile = open(pathOfFile, 'w')
inputNumber = float(input("Type a float number: "))

while (inputNumber != 0):
    realNumberFile.write("{0:.3f}\n".format(inputNumber))
    inputNumber = float(input("Type a float number: "))

realNumberFile.close()
