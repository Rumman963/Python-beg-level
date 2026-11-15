str1 = input("enter the string:")

def capitalize_words(str1):
    words = str1.split()
    for ch in range(len(words)):
        words[ch] = words[ch].capitalize()
    return ' '.join(words)

print(capitalize_words(str1))
