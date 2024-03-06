import sqlite3
pathToDb = './cap.8/db/gym.db'

def ShowCourses():
    '''
    - Show the course in a formated output

    '''
    isSql = "SELECT * FROM gymCourses"
    toCursor.execute(isSql)
    getData = toCursor.fetchall()

    print("\nDatabase query")
    print("-" * 49)
    print("{:7} {:30} {:>11}".format("Code", "Course name", "Value Month"))
    print("-" * 49)

    for data in getData:
        print("{:<7} {:30} {:>10.2f}".format(data[0], data[1], data[2]))

    print("-" * 49)
    print("Were found {} registers".format(len(getData)))

def DeleteCourse(codeParam):
    '''
    - Delete the course
    '''
    isSql = '''
    SELECT Count(codeCourse) FROM gymCourses
    WHERE codeCourse = :param
    '''

    codeParamObject = {'param': codeParam}
    
    toCursor.execute(isSql, codeParamObject)
    
    toReference = toCursor.fetchone()
    print(toReference[0])

    if toReference[0] == 0:
        return "Course {} don't exist.".format(codeParam)
    else:
        isSql = "DELETE FROM gymCourses WHERE codeCourse = :param"
        toCursor.execute(isSql, codeParamObject)
        toConnect.commit()
        return "Course {} deleted.".format(codeParam)

toConnect = sqlite3.connect(pathToDb)
toCursor = toConnect.cursor()

while True:
    ShowCourses()
    print("To exclude a course type its code")
    print("To leave program type 0 (zero)")

    inputOption = int(input("Your choice >> "))
    if inputOption == 0:
        break
    else:
        deleteMessage = DeleteCourse(inputOption)
        print(deleteMessage)

        toContinue = input("Press enter to continue...")

toCursor.close()
toConnect.close()
