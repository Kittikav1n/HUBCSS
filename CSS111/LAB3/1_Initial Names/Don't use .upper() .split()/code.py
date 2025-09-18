name = input("INPUT NAME: ")

def Separate_words(text):
    word = []
    space_str = ""
    for char in text:
        if char == " ":
            if space_str:
                word.append(space_str)
            space_str = ""
        else:
            space_str += char
    if space_str:
        word.append(space_str)
    return word
list_of_words = Separate_words(name)

result = ""
for each_word in list_of_words:
    result += each_word[0] + "."
final_result = result[:-1]

def my_upper(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

upper = my_upper(final_result)
print("List of each word:", list_of_words)
print(upper)