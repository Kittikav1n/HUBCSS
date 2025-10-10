#sum_even_numbers
def sum1(number):
    return sum([num for num in number if num % 2 == 0])

print(f"total =  {sum1([1, 2, 3, 4, 5, 6])}")
print(f"total =  {sum1([10, 21, 33, 44])}")
print(f"total =  {sum1([1, 3, 5])}")
print(f"total =  {sum1([])}")
#palindrome
def is_palindrome(text):
    s = "".join(filter(str.isalnum, text)).lower()
    return s == s[::-1]
print(f"ผลลัพธ์: {is_palindrome('A man a plan a canal Panama')}")
print(f"ผลลัพธ์: {is_palindrome('hello')}")
print(f"ผลลัพธ์: {is_palindrome('Racecar')}")
print(f"ผลลัพธ์: {is_palindrome('No lemon, no melon.')}")