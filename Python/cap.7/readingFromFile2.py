totalAmount = 0
totalCounter = 0
pathOfFile = './cap.7/files/NumbersToRead.txt'

for sequentialRead in open(pathOfFile):
    numbersReaded = int(sequentialRead)
    totalAmount += numbersReaded
    totalCounter += 1
    print("Element {} = {}".format(totalCounter, numbersReaded))

print("Total: {}".format(totalAmount))
