str1 = input("enter the string:")

def char_frequency(str1):
    seen = ""
    for ch in str1:
        if ch not in seen:
            print(f"{ch}:{str1.count(ch)}")
            seen+=ch
char_frequency(str1)