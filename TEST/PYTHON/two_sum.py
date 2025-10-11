def two_sum(num: list[int], target: int):
    sum_ = target
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] + num[j] == target:
                return num[i], num[j]
print(f"{two_sum([1, 2, 3], 3)}")