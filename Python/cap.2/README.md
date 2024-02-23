Objects and commands
=

In consensus in Software Engineer, all program needs to be able to store some data, work in it, and return it efficiently.

In Python, this concept is in variable/object. One variable stores data in memory and turns it able to be manipulated by the application.

### Objects and classes

#### Variables

Variables are designed to get and retain a group of data to be manipulated by the application ahead.

For programmer: variable is a name that has data. For a computer: a variable is an address in memory where the data are located. Variables in Python can be called/associated as an Object _(Python is a weakly typed language)._

#### Example of a simple algorithm

A simple example to demonstrate the base and height of a rectangle.

```py
>>> baseValue = 10 # intrinsic int
>>> heightValue = 4 # intrinsic int

>>> calcAreaValue = baseValue * heightValue # intrinsic int

>>> print(calcAreaValue)
40

```
Python is a weakly typed language and the majority of your type data are set intrinsically on the data.

Example of an intrinsic typed structure on a variable.

```py
>>> MyObject = 10
>>> type(MyObject)

#output: <class 'int'>
```

The term <u>Objects</u> in Python is the same as a variable and stores the data and behaves as your type. In Python variables and objects are the same things.

### Data type in Python

#### Number
- Number `<int>`
- Number `<float>`
- Number `<complex>`

#### String
- String `<str>`

#### Array
- Array `<list>`
- Tuple `<tuple>`
- Set `<set/fronzenset>`
- Dictionary `<dict>`

In Python, data can be mutable and immutable. This refers to the location in memory. The immutable objects in memory don't change your value. Instead, a new object is created and the previous one is deleted.

Each variable gets an <u>identity</u> when it's created in memory. See the example:

```py
>>> myObjExample = 10
>>> id(myObjExample)
10781960

# A new reference will be created. The previous will be deleted on memory.
>>> myObjExample = 25
>>> id(myObjExample)
10782440

```

### Identifiers

Identifiers (variable / objects) can't start with a number but can start with __(underscore), uppercase or lowercase characters. The identifiers are case-sensitive by rule.

Example of assignments

```py
>>> A = 10 # A is an indentifier and get the value 10
>>> id(A)
10781960

>>> B = A # B is created and get A
>>> id(B)
10781960 # ID of B is the same as A because it's referenced on a same path in memory

>>> C = D = E = 50 # All identifiers has the same value and ID
>>> F, G, H = 10, 20, 30 # Positional assignment 
```

### Arithmetic expression

Example of arithmetic expression in Python

```py
>>> A = 14
>>> B = 5

>>> C = A + B 
>>> print(C)
19

>>> D = A - B
>>> print(D)
9

>>> E = A * B
>>> print(E)
70

>>> F = A / B
>>> print(F)
2.8

>>> G = A // B
>>> print(G)
2

>>> H = A % B
>>> print(H)
4

>>> I = A ** B
>>> print(I)
537824

# Incremental operators
>>> A += 2 
16

>>> A -= 2
12

>>> B *= 2
10

...

```

### Print string format

Method **print()** with some possible format of output:

```py
>>> A = 10
>>> print(id(A))
10

>>> B = A
>>> print(id(B))
10

>>> C = D = E = 50
>>> print("C:{0} D:{1} E:{2}".format(C, D, E)) # deprecated formated
C:50 D:50 E:50

>>> F, G, H = 10, 20, 30 
>>> print("F:%d G:%d H:%d" %(F, G, H))
F:10 G:20 H:30

```

- Method Input gets data from the typed user
- Convert type of value: int, float, str

### Comments on Python

`#` One line comments

`"""` on the start and end lines for multiline comments
___
Have a nice code :fire:
