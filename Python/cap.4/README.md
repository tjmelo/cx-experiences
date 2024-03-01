Sequential structured types
=

Are designed sequential types: **String**, **Lists** and **Tuples**

## Strings

Strings are common in a large program language and it stores a sequence of strings. It's a sequence of characters delimited by single quotations or double quotations.

```py
S = 'Sequence of characteres with single quotations'
D = "Sequence of characteres with double quotations"

print(S)
print(D)

print(type(D)) # <class 'str'>

print(len(S)) # shows the size of string

# shows the character in the specified position
print(S[0]) # 'S'
print(S[1]) # 'e'
print(S[len(S) - 1]) # s (show the last character of the string)
```

### Backward evaluation
It's possible to do a backward evaluation in the string. The regressive evaluation is made from right to left.

```py
X = 'ABCD'

print(X[-1]) # D
print(X[-2]) # C
print(X[-3]) # B
print(X[-4]) # A
```
### String concatenation

Use the signal "+" to concatenate two sequential strings. Example:
 
 ```py
S = "Peanut"
T = "Butter"

U = S + T # Peanut Butter

U = 'I like ' + U # I like Peanut Butter

U = U + 1000 # error 
 ```

With a multiply operator and an integer numeral, the string will repeat the numeral times. Example:

```py
A = 'Peanut Butter'
B = A * 3
print(B) # Peanut Butter Peanut Butter Peanut Butter
```
### Slicing

Slicing is an important resource in Python. It gets specific parts on the string. Inside brackets, defines a start and end part of slicing a sequence `S[start:end]`

Example of how to slice a sequential string.

```py
S = 'abcdefghijklmno'
print(S) # abcdefghijlmno

print(len(S)) # 15

Sequence1 = S[3:10]
print(Sequence1) # dfghij

Sequence2 = S[0:5]
print(Sequence2) # abcde

Sequence3 = S[:4]
print(Sequence3) # abcd

Sequence4 = S[10:]
print(Sequence4) # lmno

```

There's a third format of slicing. Which defines a sequence interval to slice. Like this `S[start:end:interval]`. Example:

```py
S = 'abcdefghijklmno'
print(S[0:15:4]) # aeim

T = '9interval7interval6interval5interval'
print(T[::9]) # 98765
```
### Classes method of 'str'
Some complementaries methods of string in Python

```py
S = 'abc_123_XYZ'

print(S.lower()) # abc_123_xyz
print(S.upper()) # ABC_123_XYZ
print(S.title()) #Abc_123_XYZ
print(S.swapcase()) # ABC_123_xyz
print(S.find('123')) # 4 (position at string)
print(S.find('m')) # -1 (not found)
print(S.count('_')) # 2
print(S.replace('_', '*')) # abc*123*XYZ
print(S.replace('123', 'xpto')) # abc_xpto_XYZ
print(S.partition('_')) # ('abc', '_', '123_XYZ')
print(S.partition('*')) # ('abc_123_XYZ', '', '')
print(S.split('_')) # ['abc', '123', 'XYZ']
```

## Lists

Lists in Python are useful for storing several types of sequential data. As a type string, each allocated element can be accessed by your position in the list, it can be your size shown etc. Moreover, lists are mutable objects, in other words, your values can be changed. It might be each element in a list with a different format: object, integer, float, string, etc.

Basics operations with a list:

```py
L = [] # empty array
print(type(L)) # <class 'list'>
print(L) # It shows the list

L = [10, 'txt', 20.3, 25, 'arr'] # redefined value of array
print(L) # It shows the new values of array

print(L[0]) # 10
print(L[4]) # arr

print(len(L)) # 5

L[0] = 8 # Redefining the value
print(L) # [8, txt, 20, 25, arr]

del(L[3])
print(L) # [8, txt, 20, arr]
```

The slice commands are the same as a string. Follow the concepts with `List[start:end]` and `List[start:end:interval]`

```py
L = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]

L[0:3] # [1, 3, 5]
L[4:10] # [9, 11, 13, 15, 17, 19]
L[:5] # [1, 3, 5, 7, 9]
L[5:] # [11, 13, 15, 17, 19, 21, 23]

L[0:8:3] # [1, 7, 3]
L[::4] # [1, 9, 17]

```

It chooses a list and multiplies them by an integer number, we have a repetition that lists by the time of the number chosen. As we have seen in the example of the string.

```py
A = [3, 7] * 3
print(A) # [3,7,3,7,3,7]
```

The object function `list('string')` it's able to change a string element to a list element. Like this:

```py
# Using .list()

S = 'One text'
L = S.list(S)
print(L) # ['O','n','e',' ','t','e','x','t']

# Using .split()

S = '5 7 8.8 12'
L = S.split('') # separete by white space
print(L) # ['5', '7', '8.8', '12']
```
### In operator

With an iteration, the `in` operator allows us to verify, if there's an element in the list. It can be used in other structured data types in Python as well.

```py
L = [3, 6, 9]

9 in L # true
5 in L # false
5 not in L # true

Dogs = ['Poodle', 'Terrier', 'Buldog']
a = 'Collie'

if a in Dogs:
    print('Good chosen')
else: 
    print('We do not have this one')

# We do not have this one
```
### Methods of list

Some sequence of list's methods

```py
L = [3, 6, 7]

L.append(5)
print(L) # [3, 6, 9, 5]

L.insert(2, 15)
print(L) # [3, 6, 15, 9, 5, 2]

L.insert(99, 21)
print(L) # [3, 6, 15, 9, 5, 2, 21]

print(L.count(15)) # 1
print(L.count(45)) # 0

print(L.index(15)) # 2
print(L.index(6)) # 1
print(L.index(45)) # error

L.pop(3) # return 9 and remove it
print(L) # [3, 6, 15, 5, 2, 21]

L.remove(6) # remove the fist 6 in list
print(L) # [3, 15, 5, 2, 21]

A = [22, 32, 42]
L.extend(A)
print(L) # [3, 15, 5, 2, 21, 22, 32, 42]

L.reverse()
print(L) # [42, 32, 22, 21, 2, 5, 15, 3]

L.reverse()
print(L) # [3, 15, 5, 2, 21, 22, 32, 42]

L.sort()
print(L) # [3, 5, 15, 21, 22, 32, 42]

L.sort(reverse=True)
print(L) # [42, 32, 22, 21, 15, 5, 3]

L.clear()
print(L) # []
```
### Linked list
In Python's list, when you refer to a just created list, by another object, that new object becomes from the first object a mention, using the same `id` from memory. If necessary, to create a new copy from the first object, we can use the `.copy()` method in this object. Example:

```py
L = [2, 4, 6, 8, 10]
A = L 
print(A) # [2, 4, 6, 8, 10] (same reference id of L list)

B = L.copy()
print(B) # [2, 4, 6, 8, 10] (another reference id)
```
### Nesting list
Lists inside a list. There aren't limits to deep nesting. Example:

```py
L = [[1, 2, 3], [4, 5, 6]]

print(L[0]) # [1, 2, 3]
print(L[1]) # [5, 5, 6]

print(L[0][0]) # [1]
print(L[1][0]) # [4]
```
## Tuple
A Tuple looks like a list element but is mutable as a string. It supports nested lists as well.

Inside a tuple, the list content can be manipulated like anything. But the list, himself, can't be renamed or deleted from the tuple.

Basic operations with tuples:

```py
V = () 

print(V) # empty tuple
print(len(V)) # 0

P = 3, 6, 9
print(P) (3, 6, 9)

T = (17, 3, 'txt', 3.8)
print(type(T)) # <class 'tuple'>

print(len(T)) # 4
print(T[0]) # 17

T = T + (15, 16)
print(T) # (17, 3, 'txt', 3.8, 15, 16)

M = (0 ,1)
M = M * 6
print(M) # (0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1)
```

#### Commons error in the Tuple's definition

```py
T = (14) # considered an integet
print(type(T)) # <class 'int'>

T = (14,) #using comma inside parentesis
print(type(T)) # <class 'tuple'>
```
## Range

Examples of a range type

```py
L = list(range(10))
print(L) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

L = list(range(5, 15))
print(L) # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

L = list(range(-3, 4))
print(L) # [-3, -2, -1, 0, 1, 2, 3]

```
## For
Iteration list with `for`. Example:

```py
L = [2, 4, 6, 8, 10]
i = 0

for x in L :
    print(i, x)
    i += 1
```
The for loop receives an `else` instruction for complement. Like this:
```py
for item in sequence
    something...
else:
    something...
```
The commands `break`, `continue`, are useful in `for` loop.



