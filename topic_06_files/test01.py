nameList = []

for _ in range(3):
    name = input("What's your name: ")
    nameList.append(name)


for elem in nameList:
    print(f"Hello, {elem}")