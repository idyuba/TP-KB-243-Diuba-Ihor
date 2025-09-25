 
'''
90 - 100 A
80 - 89 B
70 - 79 C
60 - 69 D

F
'''

mark = input("Please enter the mark: ")

if mark == "A":
    print("Grade A, score >= 90 and score <= 100")
elif mark == "B":
    print("Grade B, score >= 80 and score <= 89")
elif mark == "C":
    print("Grade C, score >= 70 and score <= 79")
elif mark == "D":
    print("Grade D, score >= 60 and score <= 69")
elif mark == "F":
    print("Score under 59")
else:
    print("Mark entering ERROR")

print("Buy!")