import sqlite3
pathToDb = './cap.8/db/gym.db'

toConnect = sqlite3.connect(pathToDb)
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

isSql = '''
    insert into gymRegister
    (codePerson, namePerson, agePerson) values (1309, 'Mary Janne', 37)
'''
toCursor.execute(isSql)

toConnect.commit()
toCursor.close()
toConnect.close()
