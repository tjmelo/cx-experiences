Python + SQLite
=

In all **DBMS** (Data Base Management System) the start point is the organization of the data. This organization is named as a **Model** of a database. There are four main types:

- Hierarchical
- Network
- Relational
- Object Oriented

The relational model is the most used and it's based on a table.

**SQL** (Structured Query Language) is useful to create, store, recover and use the data in a relational database.

The database **SQLite** is compact, light, reliable and very helpful as a data repository.

> Important: In the Visual Studio was used the **SQLite Viewer** to manage the registered data in a `.db` file.

## Crating a database
A simple example of how to create a database with **SQLite** and **Python**:

```py
import sqlite3

toConnect = sqlite3.connect('pathToDb')
toCursor = toConnect.cursor()

isSql = '''
    create table gymRegister
    (codePerson integer, namePerson text, agePerson integer)
'''
toCursor.execute(isSql)

isSql = '''
    insert into gymRegister
    (codePerson, namePerson, agePerson) values (1284, 'John Doe', 32)
'''
toCursor.execute(isSql)

toConnect.commit()
toCursor.close()
toConnect.close()
```

## Getting data from the database
A simple example of getting data from a database with **SQLite** and **Python**:

```py
import sqlite3

isConnect = sqlite3.connect('pathToDb')
isCursor = isConnect.cursor()

isSql = "select * from gymRegister"
isCursor.execute(isSql)

getData = isCursor.fetchall()
isCursor.close()
isConnect.close()

for data in getData:
    print("{:<7} {:20} {:>6}".format(data[0], data[1], data[2]))

```
---
Have a good experience :fire:
