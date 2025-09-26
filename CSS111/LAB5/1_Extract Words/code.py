def extract_words(text):
    return [word for word in text.split() if len(word) >= 4]    

    #words_list = text.split(" ")
    #long_words = [word for word in words_list if len(word) >= 4]
    #return long_words

#print(extract_words(input("ENTER TEXT: ")))
print(extract_words("Don't judge a book by its cover."))
print(extract_words("All that glitters is not gold."))
print(extract_words("The multinational corporation's decentralization strategy required comprehensive reorganization of their compartmentalized departmentalization systems across intercontinental subsidiaries."))