str1 = input("enter the string:")

def count_vowels(str1):
    count= 0 
    for ch in str1.lower():
        if ch in "aeiou":
            count +=1
    return count
print(count_vowels(str1))