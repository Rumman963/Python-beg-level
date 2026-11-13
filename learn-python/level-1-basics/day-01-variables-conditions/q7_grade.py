marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid")
elif marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 55:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Grade E")