
def hello(name):
    print(f"Hello {name}")


def goodbay(name):
    print(f"GoodBay {name}")


def main():
    name = input("Please eneter your name ")
    hello(name)
    goodbay(name)

if __name__ == "__main__":
    main()