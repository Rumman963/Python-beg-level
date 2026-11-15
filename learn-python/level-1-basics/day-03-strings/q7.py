str1 = input("enter the string:")

def remove_vowels(str1):
    result=""
    for ch in str1:
        if ch.lower() not in "aeiou":
            result += ch
    return result

print(remove_vowels(str1))


