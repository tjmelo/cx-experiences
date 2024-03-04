Students = {}

print("Reading datas")

while True:
    individualRegister = int(input("Type a registration: "))

    if(individualRegister == 0):
        break
    elif individualRegister in Students:
        print("    The register has already been done    ")
        continue

    dicItem = {}
    dicItem['name'] = input("   Name: ")
    dicItem['age']= int(input("   Age: "))
    dicItem['course']= input("   Course: ")

    Students[individualRegister] = dicItem

for register, data in Students.items():
    print("    Student: {}".format(data['name']))
    print("    N° register: {}".format(register))
    print("    Age: {}".format(data['age']))
    print("    Course: {}".format(data['course']))
    print("---------------------------------------------------------")
