n = int(input("enter the number:"))
def sum_of_digits(n):
        total=0
        while n>0:
                total +=n%10
                n=n//10
        return total

print(f"sum of digits of {n} is {sum_of_digits(n)}")