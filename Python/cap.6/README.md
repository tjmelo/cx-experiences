Non-sequential structured types
=

## Hashable
An element is considered _hashable_ when it gets a hash identifier that follows it along your life cycle in the application. Thus, it can be matched with another object to verify your equality. For example:

```py
T = "Some text"
print(id(T)) # 140069661918256
print(hash(T)) # -7379016230777419689

Z = "Some text"
print(id(Z)) # 140069661918256
print(hash(Z)) # -7379016230777419689

# So
T == Z # true

L = [1, 2, 3]
print(hash(L))

L = [1, 2, 3]
print(hash(L)) # error 
# lists are unhashable type because your mutability
```
> All mutable object is considered a unhashable

## Sets
The sets allow us to create an unordered list of values whose values don't repeat. That list can be created by instructions `set` and `frozenset`.

Examples of how to create sets:

```py
A = {1, 2, 3, 4, 5, 5, 5, 5}
print(A) # {1, 2, 3, 4, 5}

B = set("12345")
print(B) # {'1','4','5','3','2'}

C = set()
print(C) # ()
```
Example of no-repeatable value in sets.
```py
L = [3, 7, 9, 16, 3, 8, 14, 9, 25]

SetsL = set(L) # convert the list to a sets
print(SetsL) # { 3, 7, 9, 16, 8, 14, 25 }

L = list(setsL)
print(L) # { 3, 7, 9, 16, 8, 14, 25 }
```

#### Operations with sets

The available operations in sets:
- Difference `a - b`
- Union `a | b`
- Intersection `a & b` 
- Symmetric difference `a ^ b`
- Belongs `value in a`
- Not belongs `value not in a`

Examples:

```py
A = set("pineapple")
print(A) # {'n', 'a', 'l', 'p', 'i', 'e'}

B = set("orange")
print(B) # {'o', 'n', 'a', 'g', 'e', 'r'}

print(A - B) # {'l', 'i', 'p'}
print(A | B) # {'r', 'a', 'g', 'p', 'o', 'e', 'n', 'l', 'i'}
print(A & B) # {'e', 'n', 'a'}
print(A ^ B) # {'r', 'g', 'o', 'p', 'l', 'i'}

print('p' in A) # true
print('o' in A) # false

```

#### Available methods

Below there're some available methods to be used in sets:

```py
A = {1, 2, 3, 4, 5, 6}

A.add(7) # add a new element
A.add(8) # add another element

B = {2, 4, 6}
B.issubset(A) # true

A.issubset(B) # false
A.issuperset(B)  # B is in A

C = A.difference(B) # like a-b
print(C) # {1, 3, 5, 7, 8}

X = 5

A.remove(X)
print(A) # {1, 2, 3, 4, 6, 7, 8}
A.pop() # 1
print(A) # {3, 7, 8}

A.isdisjoint(b) # A and B intersection is empty
L = [5, 9, 'a']

print(A.union(L)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 'a'}
```

#### Sets with Iterators

Sets can be used with iterators

```py
cont = 1
c = { 1, 2, 3, 4, 5 }

for x in c:
    print("Element {} in sets = {}".format(cont, x))
    cont += 1

'''
Element 1 in sets = 1
Element 2 in sets = 2
Element 3 in sets = 3
Element 4 in sets = 4
Element 5 in sets = 5

'''
```
## Dictionaries
Dictionaries have elements with keys and associated values. The keys and values are used as a reference to access and insert new elements in sets. Example:

```py
D = {442: "Element 442", 513: "Element 513"}
print(D) # {442: "Element 442", 513: "Element 513"}

print(D[442]) # Element 442
print(D[513]) # Element 513

D[377] = "Element 377" # adding a new element in dictionary
print(D) # {442: "Element 442", 513: "Element 513", 377: "Element 377"}

D['ab'] = (2, 4, 6)
print(D) 
# {442: "Element 442", 513: "Element 513", 377: "Element 377", 'ab': (2, 4, 6)}
```
#### Dictionaries as an iterator
Dictionaries can be used as a iterator. There are a lot of ways to create an iterator with it. One example:

```py
D = {
    1: 'Strawberry',
    2: 'Avocado',
    3: 'Apple',
    4: 'Banana'
}

# One way
for x in D : # .keys() is defult
    print(x, ' - ', D[x])

'''
1 - Strawberry
2 - Avocado
3 - Apple
4 - Banana

''' 

# Another way with .keys()
# when there isn't any specification, .keys() is default
for x in D.keys() :
    print(x, ' - ', D[x])

'''
1 - Strawberry
2 - Avocado
3 - Apple
4 - Banana

''' 

# Another way with ;.values()
for x in D.values() :
    print('Value: - ', x])

'''
Value: - Strawberry
Value: - Avocado
Value: - Apple
Value: - Banana

''' 

# Another way with .items()
for number, name in D.items() :
    print(number, ' - ', name)

'''
1 - Strawberry
2 - Avocado
3 - Apple
4 - Banana

''' 
```
