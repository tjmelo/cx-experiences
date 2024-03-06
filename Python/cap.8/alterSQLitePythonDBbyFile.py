import sqlite3

pathToDataFile = './cap.8/include/HightWeight.txt'
pathToDb = './cap.8/db/gym.db'

toReadFile = open(pathToDataFile, 'r')
listReadData = toReadFile.readlines()
toReadFile.close()

print("\n Lines file")
isSql = '''
update gymRegister set weightPerson = ?, hightPerson = ?
where codePerson = ?
'''

toConnect = sqlite3.connect(pathToDb)
toCursor = toConnect.cursor()

for item in listReadData:
    dataItem = item.rstrip()
    dataItem = dataItem.split(";")
    toCursor.execute(isSql, (dataItem[1], dataItem[2], dataItem[0]))
    toConnect.commit()
    print(dataItem,"    ...processing")

toCursor.close()
toConnect.close()
