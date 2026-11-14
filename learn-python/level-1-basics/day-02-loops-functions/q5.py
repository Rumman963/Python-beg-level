n = int(input('enter the number:'))
def reverse_number(n):
    rev = 0
    while n >0:
        rev = n%10 + rev*10
        n=n//10
    return rev

print(f"reverse of {n} is {reverse_number(n)}")

