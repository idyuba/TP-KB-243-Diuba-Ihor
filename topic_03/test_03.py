print(">>> Hello! <<<")

while True:
    cnt = int(input("Please enter cnt for barking: "))
    if cnt < 0:
        print("Error. Negative number.")
        continue
    else:
        break

for _ in  range(cnt):
    print("bark")


print(">>> Buy! <<<")