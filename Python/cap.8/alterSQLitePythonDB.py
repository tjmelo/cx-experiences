import sqlite3
pathToDb = './cap.8/db/gym.db'

toConnect = sqlite3.connect(pathToDb)
toCursor = toConnect.cursor()

isSql = "alter table gymRegister add coursePerson integer"
toCursor.execute(isSql)

isSql = "alter table gymRegister add dateInPerson date"
toCursor.execute(isSql)

isSql = "alter table gymRegister add weightPerson double"
toCursor.execute(isSql)

isSql = "alter table gymRegister add hightPerson double"
toCursor.execute(isSql)

isSql = "update gymRegister set coursePerson = 10, dateInPerson = '01/03/2024'"
toCursor.execute(isSql)

toConnect.commit()
toCursor.close()
toConnect.close()
print("Updated with success...")
