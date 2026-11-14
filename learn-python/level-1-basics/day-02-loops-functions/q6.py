n = int(input("enter the number:"))
total = 0
def sum_of_digits(n):
        while n>0:
                global total
                total +=n%10
                n=n//10
        return total

print(f"sum of digits of {n} is {sum_of_digits(n)}")