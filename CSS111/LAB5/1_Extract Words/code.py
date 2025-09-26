def extract_words(text):
    
    words_list = text.split(" ")
    long_words = [word for word in words_list if len(word) >= 4]
    return long_words

print(extract_words(input("ENTER TEXT: ")))