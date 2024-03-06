import sqlite3
pathToDb = './cap.8/db/gym.db'

toConnect = sqlite3.connect(pathToDb)
toCursor = toConnect.cursor()

# creating a new table
isSql = '''
CREATE TABLE gymCourses
(
    codeCourse INTEGER NOT NULL PRIMARY KEY,
    nameCourse TEXT,
    valueMonthCourse DOUBLE
)
'''
toCursor.execute(isSql)
print("\n   ...courses table created")

isSql = '''
INSERT INTO gymCourses 
(codeCourse, nameCourse, valueMonthCourse) values (?, ?, ?)
'''

coursesData = [
    (10, 'Bodybuilding', 70.00),
    (11, 'Aerobic training', 70.00),
    (12, 'Combo 1: Bodybuilding + Aerobic training', 110.00),
    (13, 'Swimming', 110.00),
    (14, 'Pilates', 100.00),
    (15, 'Combo 2: Pilates + Aerobic training', 180.00),
    (16, 'Crossfit', 110.00),
    (17, 'Muay Thai', 90.00),
    (18, 'Jiu Jitsu', 80.00),
    (19, 'Boxing', 80.00)
]

print("\n   ...data to be loaded")

for data in coursesData:
    print(" ", data)

toCursor.executemany(isSql, coursesData)
toConnect.commit()

toCursor.close()
toConnect.close()

print("\nTable created with success!")
