def find_max(num: list[int]):
    maxval = num[0]
    minval = num[0]
    
    for i in range(1, len(num)):
        if maxval < num[i]:
            maxval = num[i]
    
        if minval > num[i]:
            minval = num[i]
    
    return maxval, minval;

find_max,find_min = find_max([1, 2, 3])
print(f"MAX: {find_max} MIN: {find_min}")