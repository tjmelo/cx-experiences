'''
App proposed (1):
- Get fixed emloyee value earn : 500.00
- Get value sold by employee: 12398.00
- Input value commission on a total sold by employee: 6%
- Output: Fixed value plus comission to employee

'''

print('Start App 1')

howMuchSell = input('How much has the employee sold? ')

valueFixed = 500.00
valueSales = float(howMuchSell)
valueComission = 6 / 100 # 6%

valueComissionWithFix = valueComission * valueSales
valueInvoice = valueFixed + valueComissionWithFix

print("Base value: %d" %(valueFixed))
print("Comission: %d" %(valueComissionWithFix))
print("Invoicing of month: {0:.2f}".format(valueInvoice))
