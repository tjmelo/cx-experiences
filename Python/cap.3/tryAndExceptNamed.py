try:
    A = int(input('Type a first numeral value: '))
    B = int(input('Type a secondnumeral value: '))

    R = A / B 

    if A < 0:
        C = cos(A)

    print("Result: R = %.1f" % R)

except ZeroDivisionError: # Get the name of error and except it
    print("Second value can't be zero")

except ValueError: # Get the name of error and except it
    print("Type a numeral value for first and second values")

except
    print("Unknown error. It's not possible to calculate")
