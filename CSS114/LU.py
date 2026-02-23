import numpy as np

np.set_printoptions(precision=4, suppress=True)

#----------- แยกLU -----------
def LU_split(A):
    n =len(A)
    L = np.eye(n) # สร้างเมทริกซ์ L เป็นเอกลักษณ์
    U = np.zeros((n, n)) # สร้างเมทริกซ์ U เป็นศูนย์

    for k in range(n): # k = pivot ปัจจุบัน , loop แถว k
        for j in range(k, n): # loop คอลัมน์ j ตั้งแต่ k ถึง n-1
            U[k, j] = A[k, j] - np.dot(L[k, :k], U[:k, j]) # คำนวณ U
            # U[k,j] = A[k,j] - (L แถว k × U คอลัมน์ j (ผลก่อนหน้า))


        for i in range(k + 1, n): # loop ขยับแถว
            if U[k, k] == 0: # เช็ค pivot เป็น 0 
                raise ValueError("Pivot เป็น 0 ไม่สามารถแยก LU ได้") # แจ้ง error
            
            L[i, k] = (A[i, k] - np.dot(L[i, :k], U[:k, k])) / U[k, k] # คำนวณ L
            #L[i,k] = (A[i,k] - ผลก่อนหน้า) / U[k,k]
    return L, U

#----------- หาคำตอบ -----------
def LU_solve(L, U, b):
    n = len(L)
    # Ly = b
    y = np.zeros(n)
    for i in range(n): # หาค่า y ตั้งแต่แถวบนลงล่าง
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i] # แก้สมการหา y
    """
    L = [1 0 0]
        [l 1 0]
        [l l 1]
    """
    # Ux = y
    x = np.zeros(n)
    for i in range(n - 1, -1, -1): # หาค่า x ตั้งแต่แถวล่างขึ้นบน
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i] # แก้สมการหา x

    """
    U = [u u u]
        [0 u u]
        [0 0 u]
    """


    return x


#----------- main -----------
if __name__ == "__main__":

    # Matrix A 
    A = np.array([
    [1, 1, 1, 1],
    [1, 2, 3, 4],
    [1, 3, 6, 10],
    [1, 4, 10, 20]
    ], dtype=float)

    # Vector b
    b = np.array([4, 10, 20, 35], dtype=float)

    print(f"Matrix A:\n{A}\n")
    print(f"Vector b: {b}\n")
    print("-" * 30)

    L, U = LU_split(A) # แยกร่าง A เป็น L, U
    x = LU_solve(L, U, b) # เอา L, U, b ไปหาคำตอบ x

    # 3. แสดงผลลัพธ์ออกมาดู
    print(f"\nMatrix L:\n{L}")
    print(f"\nMatrix U:\n{U}")
    print("")
    print("-" * 30)
    print(f"\nx: {x}")