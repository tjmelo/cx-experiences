def Operations(x, y):
    ad = x + y
    su = x - y
    mu = x * y
    di = x / y

    return ad, su, mu, di

exampleA = int(input("Type a value to A: "))
exampleB = int(input("Type a value to B: "))

result = Operations(exampleA, exampleB)
print(result)
