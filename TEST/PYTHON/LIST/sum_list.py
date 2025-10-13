def find_sum(nums: list[int]):
    total = 0
    for num in nums:
        total += num
    return total

print(f"Total: {find_sum([1, 2, 3])}")