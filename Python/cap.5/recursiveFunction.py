def Fatorial(N):
    if N <= 1:
        return 1
    else:
        return N * Fatorial(N-1)

inputNumber = int(input("Type a number: "))
isFatorial = Fatorial(inputNumber)

print("The fatorial of {} is {}".format(inputNumber, isFatorial))
