A = int(input("Type a value for A: "))
B = int(input("Type a value for B: "))
C = int(input("Type a value for C: "))

if A <= B and A <= C:
    if B <= C:
        print("Ascending order: {}, {}, {}".format(A, B, C))
    else:
        print("Ascending order: {}, {}, {}".format(A, C, B))
elif B <= A and B <= C:
    if A <= C:
        print("Ascending order: {}, {}, {}".format(B, A, C))
    else:
        print("Ascending order: {}, {}, {}".format(B, C, A))
else:
    if A <= B:
        print("Ascending order: {}, {}, {}".format(C, A, B))
    else:
        print("Ascending order: {}, {}, {}".format(C, B, A))

