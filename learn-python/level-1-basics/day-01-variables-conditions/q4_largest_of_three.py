num1 = int(input("enter first number: "));
num2 = int(input("enter second number: "));
num3= int(input("enter third number: "));


if num1>=num2 and num1>=num3:
    print("largest number is num1:", num1);
elif num2>=num3:
    print("largest number is num2:" , num2);
else:
    print("largest number is num3:", num3);