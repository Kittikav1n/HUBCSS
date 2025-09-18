menu = {1: 25, 2: 30, 3: 35}
total_price = 0
total_cups = 0
while True:
    num_menu = int(input())
    if num_menu == 0:
        break
    cub = int(input())
    total_price += menu[num_menu] * cub
    total_cups += cub

if total_price >= 300:
    final_price = total_price * 0.95
if total_cups >= 10:
    final_price = total_price * 0.90
if total_cups >= 10 and total_price >= 300:
    total_price *= 0.90
    total_price *= 0.95

final_price = total_price
final_price = int(final_price)
print(final_price)