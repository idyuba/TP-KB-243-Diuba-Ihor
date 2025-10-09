try:
    str = input("What's A: ")
    a = int(str)
    str = input("What's B: ")
    b = int(str)
    result = a / b
    print(result)
except Exception as ex:
    print(type(ex))
    print(ex)