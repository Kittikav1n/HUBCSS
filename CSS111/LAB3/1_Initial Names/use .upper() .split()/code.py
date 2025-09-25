name = input("INPUT NAME: ")
name_split = name.split()

result = ""
for each_word in name_split:
    result += each_word[0] + "."
final_result = result[:-1]
final_upper = final_result.upper()
print(name_split)
print(final_upper)