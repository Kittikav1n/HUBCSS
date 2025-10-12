def fibo(num):
    a = 0
    b  = 1
    print(a)
    for i in range(2, num+1):
        next_ = a + b
        a = b
        b = next_
        print(b)
fibo(10)
print()
fibo(5)