input_string = input("ENTER NUMBER: ")
num = input_string.split()
number_list = []
for i in num:
    int_number = int(i)
    number_list.append(int_number)
unique_num = list(set(number_list))#ตัดตัวเลขที่ซ้ำกัน
max_num = float('-inf')
second_max_num = float('-inf')
for num in unique_num:#วนลูปเพื่อหาค่าที่มากที่สุดสองอันดับแรก
    if num > max_num:
        second_max_num = max_num
        max_num = num
    elif num > second_max_num:
        second_max_num = num

print("Second largest distinct number:", second_max_num)