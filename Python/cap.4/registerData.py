listProduct = []

someProduct = (12336, 'Liquid soap', 1337, 1.37)
listProduct.append(someProduct)

anotherProduct = (13446, 'Rice 1kg', 3554, 2.65)
listProduct.append(anotherProduct)

thirtyProduct = (13956, 'Bean 1kg', 439, 2.10)
listProduct.append(thirtyProduct)

print('------------------------- Database -------------------------')
print(listProduct)
print('------------------------------------------------------------')

codeP, nameP, qtdeP, PrUnit = listProduct[1];

print(codeP)
print(nameP)
print(qtdeP)
print(PrUnit)
