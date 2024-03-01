listOfProducts = []

firstProduct = (12336, 'Liquid soap', 1337, 1.37)
listOfProducts.append(firstProduct)

secondProduct = (13446, 'Rice 1kg', 3554, 2.65)
listOfProducts.append(secondProduct)

thirtyProduct = (13956, 'Bean 1kg', 439, 1.19)
listOfProducts.append(thirtyProduct)

print("List of storaged products\n")

for (pcod, pname, pqty, punit) in listOfProducts:
    print("Product identification: ", pcod)
    print("Product description: ", pname)
    print("Product store: {0} by {1:.2f}".format(pqty, punit))
    print("Total of this product: {0:.2f}".format(pqty * punit))
    print("----------------------------------------------------------")
