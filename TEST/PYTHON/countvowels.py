#countvowels
def countvowels(text):
    s = "".join(filter(str.isalnum, text)).lower()
    count = 0;
    for char in s :
        if char in "aeiou":
            count = count +1
    return count;
print(f"ผลลัพธ์: {countvowels('Hello World')}")
print(f"ผลลัพธ์: {countvowels('Python Programming')}")
print(f"ผลลัพธ์: {countvowels('AEIOUaeiou')}")
print(f"ผลลัพธ์: {countvowels('Rhythm')}")