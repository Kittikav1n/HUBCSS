def evens(nums: list[int]):
    find_even = []
    for i in nums:
        if i % 2 == 0:
            find_even.append(i)
    return find_even;
num  = list(map(int, input("num:").split()))
find = evens(num)
print(f"Evens: {find}") 