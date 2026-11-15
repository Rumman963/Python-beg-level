str1=input("enter the string:")
def reverse_string(str1):
    reverse_str=""
    for ch in str1:
        reverse_str = ch + reverse_str
    return reverse_str
print(reverse_string(str1))    


    
