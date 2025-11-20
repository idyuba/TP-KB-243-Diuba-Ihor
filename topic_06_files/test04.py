studentList = []

with open("Book1.csv") as file:
    for line in file:
        name, mark = line.rstrip().split(",")
        #student = {}
        #student["name"] = name
        #student["mark"] = mark
        #student = {"name":name, "mark":mark}
        #studentList.append(student)
        studentList.append({"name":name, "mark":mark})

def getName(student):
    return student["name"]

def getMark(student):
    return student["mark"]


for elem in sorted(studentList, key=getMark):
    print(f"Name = {elem['name']}  mark = {elem["mark"]}")

#for elem in sorted(studentList, key=lambda student: student["name"]):
#    print(f"Name = {elem['name']}  mark = {elem["mark"]}")
