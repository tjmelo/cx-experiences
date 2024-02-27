getValue = 0

while getValue < 100 or getValue > 500:
    try:
        getValue = int(input("Type a numeral value: "))
    except:
        print("%d it's not a number." % getValue)
    else:
        if getValue < 100 or getValue > 500:
            print("Typed value %d it's out of required interval." % getValue)
        else: 
            print("The value %d it's OK!" % getValue)
    finally:
        print("\n")
