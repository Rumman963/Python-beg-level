n = int(input("enter the number: "))
def is_armstrong(n):
    power = len(str(n))
    total = 0
    temp = n
    while temp >0:
        digits =  temp %10
        total += digits **power
        temp //=10
    return total == n

print(is_armstrong(n))


