import numpy as np

np.set_printoptions(precision=4, suppress=True)
# ---------- หา inverse ----------
def get_inverse(A):
    n = len(A) 
    A = A.astype(float) # แปลงเป็น float
    M = np.hstack((A, np.eye(n))) # สร้าง [A | I]

    for i in range(n): # i = ตัวชี้แถวปัจจุบัน
        pivot_row = i + np.argmax(np.abs(M[i:, i])) # ดูค่าคอลัมน์ i ตั้งแต่แถว i ลงไป

        if abs(M[pivot_row, i]) < 1e-10: # ถ้า pivot ≈ 0
            return None   # singular → inverse ไม่มี
        
        if pivot_row != i:
            M[[i, pivot_row]] = M[[pivot_row, i]] # ย้ายแถวที่ดีที่สุดมาอยู่ตำแหน่ง pivot

    
        M[i] = M[i] / M[i, i] # ทำ pivot = 1

        for k in range(n): # ทำตัวอื่นในคอลัมน์ = 0
            if k != i:
                M[k] -= M[k, i] * M[i]

    return M[:, n:]

# ---------- main ----------
if __name__ == "__main__":

#---------- Matrix A ----------
    A = np.array([
    [1 , 2, -3],
    [-1,  1, -1],
    [0, -2 , 3]
], dtype=float)
#---------- Ax = b ---------- 
#b = np.array([3, 7, 5], dtype=float)
    b = None   # ← ถ้าอยากหา inverse อย่างเดียว

    print("\nMatrix A:")
    print(A)
    print("-" * 40)

#---------- หา inverse ----------
    invA = get_inverse(A)

    if invA is None:
        print("หา Inverse ไม่ได้ (Singular Matrix)")
    else:
        print("\nA inverse:")
        print(invA)
        #print("\nตรวจสอบ A * A inverse (ควรได้ I):")
        #print(A @ invA)

#---------- b → แก้ Ax=b ----------
        if b is not None:
            x = invA @ b
            print("\nSolution x (Ax=b):")
            print(x)