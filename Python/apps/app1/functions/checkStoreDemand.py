def toCheckerStoreDemand(isReadProducts, isSales, isOutputFile):
    getStoreProducts = {}

    for codeProduct in isReadProducts.keys():
        getItem = {}
        getItem['store'] = isReadProducts[codeProduct]['store']
        getItem['qmin'] = isReadProducts[codeProduct]['qmin']
        getItem['demand'] = 0

        getStoreProducts[codeProduct] = getItem

    for itemSale in isSales:
        codeProduct = itemSale[3]
        getStoreProducts[codeProduct]['demand'] += itemSale[4]
    
    isOutputFile.write("-"*65 + "Block start -" + "\n")
    isOutputFile.write("Need for stock during the period ")
    isOutputFile.write("-"*65 + "\n")
    isOutputFile.write(" " *9 + "Store" + " " *14 + "Store" + ""*4 + "Store" + ""*6 + "Neces.\n")
    isOutputFile.write("Prod.   Initial     Demand" + " "*6 + "Final    Minimum     Purchase\n")
    
    isWrite = "{:<5} {:>10d} {:10d} {:>10d} {:10d} {:10d}\n"

    for codeProduct, data in getStoreProducts.items():
        finalStore = data['store'] - data['demand']
        
        if finalStore < 0:
            finalStore = 0
        
        necessaryPurchase = data['demand'] - data['store'] + data['qmin']

        if necessaryPurchase < 0:
            necessaryPurchase = 0

        isOutputFile.write(isWrite.format(
            codeProduct,
            data['store'],
            data['demand'],
            finalStore,
            data['qmin'],
            necessaryPurchase)
        )
    
    isOutputFile.write("-"*65)
