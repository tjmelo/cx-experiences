outputFormat = "{:>7} {:>13.2f} {:>10.2f} {:>12.2f}"
totalICMS = 0
totalAmount = 0
pathOfFile = './cap.7/files/Store.csv'

print("Product   Purch. value    ICMS       Item")
fileToRead = open(pathOfFile, 'r')

for item in fileToRead.readlines():
    item = item.rstrip()
    itemSplit = item.split(";")
    itemSplit[0] = int(itemSplit[0])
    itemSplit[1] = int(itemSplit[1])
    itemSplit[2] = float(itemSplit[2])
    itemSplit[3] = float(itemSplit[3]) / 100

    itemPurchase = itemSplit[1] * itemSplit[2]
    itemICMS = itemPurchase*  itemSplit[3]

    itemCheck = itemPurchase - itemICMS
    totalICMS += itemICMS
    totalAmount += itemCheck

    print(outputFormat.format(itemSplit[0], itemPurchase, itemICMS, itemCheck))

fileToRead.close()
print("--------------------------------------------------------------------------")
print(outputFormat.format("Totals", totalAmount+totalICMS, totalICMS, totalAmount))

