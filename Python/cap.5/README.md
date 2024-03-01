Functions
=

The functions make an important scope in a program. In Python, as another programming language, the functions are packages subroutines of algorithms, useful to several situations.

Example of a function:

```py
def Sum (X, Y):
    R = X + Y
    return R
```
The principal concept of a function is to create an independent group of commands, splitting a big and complex algorithm into small pieces. In this case, when those parts are joined, the program executes each respective block.

### Function scope

About function in Python

 - They have a required header with `def` command.
 - They need a name in the header as well.
 - There must be parentheses after their names. These parentheses can store one or more parameters.
 - The parameters are not required in a function, but the parentheses are.
 - The header ends with the `:`
 - The function body is indented to the right about the header
 - In the function body get all necessary commands of the program.

### Default params
The functions in Python can get parameters as a default. That is, if in the function, the variable caller inside a program, the argument was omitted, the function returns the result with a default value defined. Example:
> As a ruler in Python, the parameters **without** a default value must be declared at first.

```py
def Sum (X = 0, Y = 1):
    R = X + Y
    return R

# callers
A = Sum()
B = Sum(2)
```
### Named params
The parameters in the function can be named, that is, they can defined in the caller accordingly with your names. In this case, it's not necessary to follow the position order of the defined parameters. Example:

```py
def Sum (X, Y):
    R = X + Y
    return R

A = Sum(Y=2, X=3) # named params
```

### Packaging params
Even if it's not known the number of parameters sent to a function, it's possible to package all of them in a value group. As a follows:

```py
def Sum (*params):
    r = 0
    for i in params:
        r += i
        return r


A = Sum(3, 9) # 12
B = Sum(1, 2, 3, 4) # 10
```

> The **\*** is recognized as a **tuple**

### Destructuring params

```py
def getDestructureList(a, b, c):
    print(a)
    print(b)
    print(c)

L = [31, 77, 193]
getDestructureList(*L) # asterisk to destructuring
```
> To destructuing the list as a param, it needs to be exaclty the same number of params.

### Multiple returns
The functions can return several values if necessary. Example:

```py
def Operations(x, y):
    ad = x + y
    su = x - y
    mu = x * y
    di = x / y

    return ad, su, mu, di

result = Operations(5, 5)
print(result) # (10, 0, 25, 1.0)

```
### Recursive functions

Recursive functions call itself inside the application. Like this:

```py
def Fatorial(N):
    if N <= 1:
        return 1
    else:
        return N * Fatorial(N-1)

Fatorial(6)
```

