N = int(input("Type a number: "))
i = 2

while i < N:
    R = N % i

    if R == 0:
        print("%d não é primo" % N)
        break
    i += 1
else:
    print("%d é primo" % N)
