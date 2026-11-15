def is_valid_palindrome(str1):
    cleaned = ""
    for ch in str1:
        if ch.isalnum():
            cleaned += ch.lower()
    return cleaned == cleaned[::-1]

print(is_valid_palindrome("race a car"))
print(is_valid_palindrome("A man, a plan, a canal: Panama")) 