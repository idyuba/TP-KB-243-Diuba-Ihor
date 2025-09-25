 
'''
90 - 100 A
80 - 89 B
70 - 79 C
60 - 69 D

F
'''

mark = input("Please enter the mark: ")

match mark:
    case "A":
        print("Grade A, score >= 90 and score <= 100")
    case "B":
        print("Grade B, score >= 80 and score <= 89")
    case "C":
        print("Grade C, score >= 70 and score <= 79")
    case "D":
        print("Grade D, score >= 60 and score <= 69")
    case "F":
        print("Score under 59")
    case _:
        print("Mark entering ERROR")

print("Buy!")