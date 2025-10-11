#group anagrams
def group(strs):    
    group_map = {}
    for word in strs:
        key = "".join(sorted(word))
        if key in group_map:
            group_map[key].append(word)
        else:
            group_map[key] = [word]
    return list(group_map.values())
    
input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
input2 = [""]
input3 = ["a"]
print(f"{group(input1)}")
print(f"{group(input2)}")
print(f"{group(input3)}")

