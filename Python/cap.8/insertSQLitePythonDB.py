import sqlite3
pathToDb = './cap.8/db/gym.db'

def showData(param):
    '''
    Show an formated output of data in param
    '''
    print("\nDatabse query\n")
    print("Data from table")
    print("-" * 35)
    print("{:7} {:20} {:>6}".format('Code', 'Name', 'Age'))
    print("-" * 35)

    for data in param:
        print("{:<7} {:20} {:>6}".format(data[0], data[1], data[2]))

    print("-" * 35)
    print("Were found {} registers".format(len(param)))

isConnect = sqlite3.connect(pathToDb)
isCursor = isConnect.cursor()

isSql = '''
insert into gymRegister
(codePerson, namePerson, agePerson) values (?, ?, ?)
'''

print("Type the data separated by comma")
print("Code, Name, Age")

getInput = input()

while getInput != "":
    toReadData = getInput.split(',')

    try:
        isCursor.execute(isSql, toReadData)
        isConnect.commit()
    except:
        print("{} invalid data".format(toReadData))
    else:
        print(" " * 30, "...registered with success")
    finally:
        print("Code, Name, Age")
    
    getInput = input()

isSql = "select * from gymRegister"
isCursor.execute(isSql)
getData = isCursor.fetchall()
isCursor.close()
isConnect.close()

showData(getData)


