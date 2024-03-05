totalAmount = 0
totalCounter = 0
pathOfFile = './cap.7/files/NumbersToRead.txt'

fileToRead = open(pathOfFile, 'r')
sequentialRead = fileToRead.readline()

while sequentialRead != '':
    numbersReaded = int(sequentialRead)
    totalAmount += numbersReaded
    totalCounter += 1
    print("Element {} = {}".format(totalCounter, numbersReaded))
    sequentialRead = fileToRead.readline()

fileToRead.close()
print("Total: {}".format(totalAmount))
