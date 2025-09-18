number = int(input())
num = []
for i in range(number):
    num.append(int(input()))
for i in num:
    if (i % 2 != 0):
        print("T")
else:
    print("F")