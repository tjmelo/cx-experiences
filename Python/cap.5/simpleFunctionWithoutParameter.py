def functionWithoutParam():
    toReadANumber = int(input("Type a number: "))
    return toReadANumber

callerFunction = functionWithoutParam()
print("The value typed: %d" % callerFunction)
