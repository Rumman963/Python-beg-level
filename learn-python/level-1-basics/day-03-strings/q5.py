str1=input("enter the string:")

def count_words(str1):
    words = str1.split()
    return len(words)

print(count_words(str1))