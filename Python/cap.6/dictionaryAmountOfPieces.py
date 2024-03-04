amountCodePieces = {}

def toRegisterPieces():
    codPiece = int(input("Type the code of piece: "))
    
    if codPiece == 0:
        return "End of reading data"
    elif codPiece in amountCodePieces:
        print("The piece {} has already registered.".format(codPiece))
        return toRegisterPieces()
    else:
      qtyPieces = int(input("Type the quantity: "))
      amountCodePieces[codPiece] = qtyPieces
      return toRegisterPieces()

print("Reading data")
print(toRegisterPieces())
print("Store pieces")

for item in amountCodePieces:
    print("{1:4} unity of pieces {0}".format(item, amountCodePieces[item]))
