def readDataFromFile(list):
    with open("nameList.txt", "r") as file:
        for line in file:
            list.append(line.rstrip())

def printAllList(list):
    for name in list:
        print(f"Hello {name}")

def saveData(list):
    with open("nameList.txt", "w") as file:
        for name in list:
            file.write(f"{name}\n")

def main():
    nameList = []
    readDataFromFile(nameList)
    printAllList(nameList)
    print()
    temp = input("Please enter neww name: ")
    nameList.append(temp)
    printAllList(nameList)

    saveData(nameList)

main()