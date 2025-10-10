#sum_even_numbers
def sum1(number):
    return sum([num for num in number if num % 2 == 0])

print(f"total =  {sum1([1, 2, 3, 4, 5, 6])}")
print(f"total =  {sum1([10, 21, 33, 44])}")
print(f"total =  {sum1([1, 3, 5])}")
print(f"total =  {sum1([])}")