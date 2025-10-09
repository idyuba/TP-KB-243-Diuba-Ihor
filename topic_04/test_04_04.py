def getIntValue(prompt):
    while True:
        try:
            str = input(prompt)
            value = int(str)
        except:
            print(f"[ {str} ] is not integer")
        else:
            break
    return value

a = getIntValue("What's A: ")
b = getIntValue("What's B: ")

result = a + b

print(result)