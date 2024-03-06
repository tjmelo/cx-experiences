import sqlite3
pathToDb = './cap.8/db/gym.db'

isConnect = sqlite3.connect(pathToDb)
isCursor = isConnect.cursor()

isSql = "select * from gymRegister"
isCursor.execute(isSql)

getData = isCursor.fetchall()
isCursor.close()
isConnect.close()

print("\nGetting data from Gym")
print("-" * 75)
print("{:7} {:20} {:>6} {:>6} {:15} {:>6} {:>6}".format("Code", "Name", "Age", "Course", "Data In", "Weight", "Hight"))
print("-" * 75)

for data in getData:
    print("{:<7} {:20} {:>6} {:>6} {:15} {:>6} {:>6}".format(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))

print("-" * 75)
print("Were found {} registers". format(len(getData)))
