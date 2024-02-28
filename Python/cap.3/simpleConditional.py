A = int(input("Type a value for A: "))
B = int(input("Type a value for B: "))

if B == 0:
    print("It's not possible to calculate")
else:
    R = A / B
    print("Result: R = %.1f" % R)
