english_sentence = "It's suggested to walk, study, and sleep everyday; for a great health."
def my_split(text):
    words = []
    current_word = ""
    separators = [" ", ",", ";", ":"]
    for char in text:
        if char in separators:
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    return words

def my_lower(text):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result    
list_of_words = my_split(english_sentence)

lowercase_words = []
for word in list_of_words:
    lowercase_words.append(my_lower(word))

print("List of each word:", lowercase_words)

print("Number of words:", len(lowercase_words))