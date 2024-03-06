def toCheckerTotalsByProduct(isReadProducts, isSales, isOutputFile):
    getTotalProducts = {}

    for codeProduct in isReadProducts.keys():
        getItem = {}
        getItem['totalval'] = 0
        getItem['totalqty'] = 0

        getTotalProducts[codeProduct] = getItem
    
    for itemSale in isSales:
        codeProduct = itemSale[3]
        getTotalProducts[codeProduct]['totalval'] += itemSale[4] * itemSale[5]
        getTotalProducts[codeProduct]['totalqty'] += itemSale[4]

    isOutputFile.write("-"*65 + "Block start -" + "\n")
    isOutputFile.write("Total orders in backlog")
    isOutputFile.write("-"*65 + "\n")
    isOutputFile.write("Product     Total Value     Quantity     Middle Price    Cost Price     Middle Margin\n")

    isWrite = "{:<5} {:>11.2f} {:8d} {:>10.2f} {:10.2f} {:10.1f}%\n"

    isTotalSales = 0
    for codeProduct, data, in getTotalProducts.items():
        try:
            isTotalSales += data['totalval']
            isMiddlePrice = data['totalval'] / data['totalqty']
            isProfit = (isMiddlePrice / data['unitpr'] - 1) * 100
        except:
            isMiddlePrice = isProfit = 0
        
        isOutputFile.write(isWrite.format(
            codeProduct,
            data['totalval'],
            data['totalqty'],
            isMiddlePrice,
            isReadProducts[codeProduct]['unitpr'],
            isProfit
        ))
    
    isOutputFile.write("-"*65 + "\n")
    isOutputFile.write("Total {:>11.2f}\n".format(isTotalSales))
