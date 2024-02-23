Important concepts about Python
=
Python was released as a personal propose project by an excited developer Guido Van Rossum. The idea around this project was to create a **portable**, **noncomplicated**, **open-source** and especially **easy-to-learn** language.

Python was born with an audacious proposal too: to have a big aplicability. Therefore, it's intended to act on big fronts, such as software development, data analysis, database management, etc.

> _The quoted examples here are tested inside Linux OS Ubuntu_

At the moment this post was written, the language Python is in the **3.12+** version. You can check the version this way following:

> _In Linux OS, usually comes with a version installed by default_

```bash
$ python3 --version
```

The installation method is easy. Just check the documentation on the official site [python.org](https://python.org) and follow the suggested steps accordingly the enable current versions.

Furthermore, it's possible to know exactly which Python is installed in. On Ubuntu Linux, for example, if we type in the terminal the following command, it'll show the path:

```bash
$ which python3
``` 

---

### The first commands with Python

The first commands with Python can be written using the OS's terminal. Type it:

```bash
$ python3
```

The terminal turns into an **IDLE**. We can type several commands aggregated to the Python language and they'll be rendered perfectly.

Some examples of commands that we can type:

```py
>>> print('Hello World!')
Hello World!

>>> someExampleVariable = "Some important concepts about Python."
>>> print(someExampleVariable)

Some important concepts about Python.

>>> 5 + 5
10

>>> 6 * 2
12

>>> (15 + 5 + 10) * 3
90

>>> Invalid instruction to the interpreter
SyntaxError: invalid syntax

>>>|
```

#### _Integrated Development Environments_ (IDEs)

Using an **IDE** such as VSCode, Atom, Eclipse, Vim, etc, is very good advice for creating big and robust applications when working on a real project, on a squad team.

In this case, the **IDLE** is used as an optional tester command or to a specific criteria.

---

Have a nice code :fire:
