exampleString = 'abc_123_XYZ'

print(exampleString.lower()) # abc_123_xyz
print(exampleString.upper()) # ABC_123_XYZ
print(exampleString.title()) #Abc_123_XYZ
print(exampleString.swapcase()) # ABC_123_xyz
print(exampleString.find('123')) # 4 (position at string)
print(exampleString.find('m')) # -1 (not found)
print(exampleString.count('_')) # 2
print(exampleString.replace('_', '*')) # abc*123*XYZ
print(exampleString.replace('123', 'xpto')) # abc*xpto*XYZ
print(exampleString.partition('_')) # ('abc', '_', '123_XYZ')
print(exampleString.partition('*')) # ('abc_123_XYZ', '', '')
print(exampleString.split('_')) # ['abc', '123', 'XYZ']
