fistTerm = int(input("Type a first term: "))
reasonTerm = int(input("Type the PA rason: "))
quantityTerm = int(input("Type the quantity of terms: "))

listTerm = []
cont = 0

while(cont < quantityTerm):
    listTerm.append(fistTerm)

    fistTerm = fistTerm + reasonTerm
    cont += 1

print("PA resultant: ", listTerm)
