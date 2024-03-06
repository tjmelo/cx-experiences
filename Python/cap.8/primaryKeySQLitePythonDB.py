import sqlite3
pathToDb = './cap.8/db/gym.db'

print("\nCreating primary key for gymRegister table")

toConnect = sqlite3.connect(pathToDb)
toCursor = toConnect.cursor()

isSql = 'create table temp as select * from gymRegister'
toCursor.execute(isSql)

isSql = 'drop table gymRegister'
toCursor.execute(isSql)

isSql = '''
create table gymRegister (
    codePerson integer NOT NULL PRIMARY KEY,
    namePerson text,
    agePerson integer,
    coursePerson integer,
    dateInPerson date,
    weightPerson double,
    hightPerson double
)
'''
toCursor.execute(isSql)

isSql = '''
insert into gymRegister
(codePerson, namePerson, agePerson, coursePerson, dateInPerson, weightPerson, hightPerson)
select codePerson, namePerson, agePerson, course, dateIn, weight, hight from temp
'''
toCursor.execute(isSql)

toConnect.commit()

isSql = 'drop table temp'
toCursor.execute(isSql)

toCursor.close()
toConnect.close()
