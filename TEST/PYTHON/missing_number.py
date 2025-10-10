def missing_number(number):
    first = number[0]
    last = number[-1]
    list_ = range(first, last+1)

    sum_list = sum(list_)
    sum_number = sum(number)
    return sum_list - sum_number
    
print(f"number: {missing_number([1, 2, 3, 5])}")
print(f"number: {missing_number([10, 11, 13, 14, 15])}")
print(f"number: {missing_number([-2, -1, 1, 2])}")
print(f"number: {missing_number([1, 3])}")