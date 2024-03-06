pathToProductFile = './app1/include/products.txt'

def toReadProductsFile():
    isProductObject = {}
    isFile = open(pathToProductFile)

    for productString in isFile.readlines():
        productString = productString.rstrip()
        getLineString = productString.split(";")

        codeLineString = int(getLineString[0])
        
        getItem = {}
        getItem['store'] = int(getLineString[1])
        getItem['qmin'] = int(getLineString[2])
        getItem['unitpr'] = float(getLineString[3])
        getItem['pmargin'] = float(getLineString[4])
        
        isProductObject[codeLineString] = getItem

    isFile.close()
    print("\nReaded PRODUCTS.txt.")
    print("\nWere reader {} lines".format(len(isProductObject)))

    return isProductObject
