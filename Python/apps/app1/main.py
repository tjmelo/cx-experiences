from functions.presentationData import toShowPresentationData
from functions.readProducts import toReadProductsFile
from functions.readSales import toReadSalesFiles
from functions.checkStoreDemand import toCheckerStoreDemand
from functions.checkTotalByProducts import toCheckerTotalsByProduct

pathToCheckerFile = './app1/include/checker.txt'

toShowPresentationData()
isReadProducts = toReadProductsFile()
isSales = toReadSalesFiles()

isOutputFile = open(pathToCheckerFile, 'w', encoding="UTF-8")
toCheckerStoreDemand(isReadProducts, isSales, isOutputFile)
toCheckerTotalsByProduct(isReadProducts, isSales, isOutputFile)

isOutputFile.close()
