try:
    str = input("What's A: ")
    a = int(str)
    str = input("What's B: ")
    b = int(str)
    result = a / b
    print(result)
except ValueError:
    print(f"{str} value is not integer")
except ZeroDivisionError:
    print(f"ERROR: value B is zerro")

