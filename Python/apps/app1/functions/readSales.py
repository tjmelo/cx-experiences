pathToSalesFile = './app1/include/sales.txt'

def toReadSalesFiles():
    isSales = []
    isFile = open(pathToSalesFile)

    for salesString in isFile.readlines():
        salesString = salesString.rstrip()
        getLineString = salesString.split(";")

        for i in range(6):
            if i < 5:
                getLineString[i] = int(getLineString[i])
            else:
                getLineString[i] = float(getLineString[i])
        
        isSales.append(tuple(getLineString))

    isFile.close()
    print("\nReaded SALES.txt.")
    print("\nWere reader {} lines".format(len(isSales)))

    return isSales

