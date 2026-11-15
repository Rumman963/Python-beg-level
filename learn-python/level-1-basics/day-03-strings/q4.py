str1 = "Hello 123 World"

def count_types(str1):
    letters = 0
    digits = 0
    spaces = 0
    for ch in str1.lower():
        if ch.isalpha():
            letters +=1
        elif ch.isdigit():
            digits +=1
        elif ch.isspace():
            spaces +=1
    return letters , digits , spaces

print(count_types(str1))