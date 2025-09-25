print(">>> Hello! <<<")

def askNumber():
    while True:
        cnt = int(input("Please enter cnt for barking: "))
        if cnt < 0:
            print("Error. Negative number.")
            continue
        else:
            break
    return cnt

def bark(n):
    for _ in  range(n):
        print("bark")

def main():
    bark(askNumber())


main()

print(">>> Buy! <<<")