Control flow
=

### Conditional commands
#### Simple conditional command

Conditionals are essential in code to ensure do flow of code and some kind of treatment of errors. Simple example:

```py
A = int(input("Type a value for A: "))
B = int(input("Type a value for B: "))

if B == 0:
    print("It's not possible to calculate")
else:
    R = A / B
    print("Result: R = %.1f" % R)
```
- _Example of a _conditional that _tests_ if the_ value of variable `B` it's `0`_
- _Be careful about the indentation of each block of command_

#### Simple conditional command for comparison

Simple command comparison

```py
A = 15
B = 3

print(A > B) #true
print(A == B) #false
print(A + B >= 20) #false
```
#### Compound conditionals

Conditional by precedence
 ```py
 A = 15
 B = 9
 C = 9

B == C or A < B and A < C # comparison for true 

(B == C or A < B) and A < C # comparison for false

 ```

 _The example above uses the conditional by precedence_


#### Complete conditional command

Example of a complete conditional command with declaration `elif`

```py
PH = 8.5

if PH < 7.0:
    print('Acid solution')
elif PH === 7.0:
    print('Neutral solution')
else: 
    print('Basic solution')

```
#### Conditional loop

```py
print("Start program")

Cont = 1

while Cont <= 10:
    print(Cont)
    Cont += 1 # or Cont = Cont + 1

print("End program")

```

#### Try / except

Execute a condition and in case no expected value, the program gets an output error as an except. Example:

```py
A = 5
B = 0

try:
    R = A / B
    print("Result: R = %.1f" % R)
except:
    print("It's not possible to calculate.") # Get a error
```




---
Have a nice code :fire:
