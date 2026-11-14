n = int(input("enter the no:"))

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print(is_prime(n))


for i in range(1 , 51):
    if is_prime(i):
        print(i, end=' ')

