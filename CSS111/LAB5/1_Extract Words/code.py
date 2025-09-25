def extract_words(text):
    words_list = text.split(" ")
    long_words = [] 
    for word in words_list:
        if len(word) > 4:
            long_words.append(word)
    return long_words

print(extract_words(input("ENTER TEXT: ")))