name = input("What's your name: ")
with open("nameList.txt", "a") as file:
    file.write(f"{name}\n")