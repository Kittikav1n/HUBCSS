#palindrome
def is_palindrome(text):
    s = "".join(filter(str.isalnum, text)).lower()
    return s == s[::-1]
print(f"ผลลัพธ์: {is_palindrome('A man a plan a canal Panama')}")
print(f"ผลลัพธ์: {is_palindrome('hello')}")
print(f"ผลลัพธ์: {is_palindrome('Racecar')}")
print(f"ผลลัพธ์: {is_palindrome('No lemon, no melon.')}")
