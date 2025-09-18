number = int(input(""))
A = list(map(int,input("").split()))
if (number %2 == 0):
    index1 = (number // 2)-1
    index2 = (number // 2)
    MD = (A[index1] + A[index2]) / 2
    print(f"{MD:.2f}")
else :
    index1 = (number // 2)
    MD = A[index1]
    print(f"{MD:.2f}")