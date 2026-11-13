marks = int(input("enter marks:"));

if marks>=90:
    print("Grade A");
elif marks>=75 and marks<90:
    print("Grade B");
elif marks>=55 and marks<75:
    print("Grade C");
elif marks>=35 and marks<55:
    print("Grade D");
elif marks<35 and marks>=0:
    print("Grade E");
elif marks<0 or marks>100:
    print("Invalid");


