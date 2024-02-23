'''
App proposed (3):

 - Input: The the name of a any product
 - Input: Quantity sold of this product
 - Input: Unity value of this product

 - Output: Total value of this product

Repeat the above process 3x

 - Output: Total of all products sold

'''

getProduct1 = input('Type the sold product: ')
getQuantitySold1 = input('Type the quantity sold: ')
getUnitaryValueOfProduct1 = input('Type the unitary value of product: ')

getResultOfProduct1 = int(getQuantitySold1) * float(getUnitaryValueOfProduct1)

print('Product: {0} - {1:.2f}'.format(getProduct1, getResultOfProduct1))

#----------------------------------------------------------------------
print('------------------------------------------------------------------')

getProduct2 = input('Type the sold product: ')
getQuantitySold2 = input('Type the quantity sold: ')
getUnitaryValueOfProduct2 = input('Type the unitary value of product: ')

getResultOfProduct2 = int(getQuantitySold2) * float(getUnitaryValueOfProduct2)

print('Product: {0} - {1:.2f}'.format(getProduct2, getResultOfProduct2))

#----------------------------------------------------------------------
print('------------------------------------------------------------------')

getProduct3 = input('Type the sold product: ')
getQuantitySold3 = input('Type the quantity sold: ')
getUnitaryValueOfProduct3 = input('Type the unitary value of product: ')

getResultOfProduct3 = int(getQuantitySold3) * float(getUnitaryValueOfProduct3)

print('Product: {0} - {1:.2f}'.format(getProduct3, getResultOfProduct3))

#----------------------------------------------------------------------
print('------------------------------------------------------------------')

totalOfAllProductsSold = getResultOfProduct1 + getResultOfProduct2 + getResultOfProduct3
print('Total of all product sold: {0}'.format(totalOfAllProductsSold))
