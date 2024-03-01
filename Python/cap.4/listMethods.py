L = [3, 6, 7]

L.append(5)
print(L)

L.insert(2, 15)
print(L)

L.insert(99, 21)
print(L)

print(L.count(15)) # 1
print(L.count(45)) # 0

print(L.index(15)) # 2
print(L.index(6)) # 1
# print(L.index(45)) # error

L.pop(3)
print(L)

L.remove(6)
print(L)

A = [22, 32, 42]
L.extend(A)
print(L)

L.reverse()
print(L)

L.reverse()
print(L)

L.sort()
print(L)

L.sort(reverse=True)
print(L)

L.clear()
print(L)
