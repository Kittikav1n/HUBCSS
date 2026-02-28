def gaussian_elimination(A):
    n = len(A)
    m = len(A[0])

    # ===== Forward Elimination =====
    for k in range(n):

        # Pivoting
        max_row = max(range(k, n), key=lambda i: abs(A[i][k]))
        A[k], A[max_row] = A[max_row], A[k]

        if abs(A[k][k]) < 1e-10:
            continue

        # ทำให้ด้านล่าง pivot เป็น 0
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, m):
                A[i][j] -= factor * A[k][j]

    # ===== ตรวจผลลัพธ์ =====
    rank = 0
    for i in range(n):
        if any(abs(A[i][j]) > 1e-10 for j in range(n)):
            rank += 1
        elif abs(A[i][n]) > 1e-10:
            return "No solution"

    if rank < n:
        return "Infinite solutions"

    # ===== Back Substitution =====
    x = [0]*n
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x


def gauss_jordan(A):
    n = len(A)
    m = len(A[0])

    for k in range(n):

        # Pivoting
        max_row = max(range(k, n), key=lambda i: abs(A[i][k]))
        A[k], A[max_row] = A[max_row], A[k]

        if abs(A[k][k]) < 1e-10:
            continue

        # Normalize pivot = 1
        pivot = A[k][k]
        for j in range(m):
            A[k][j] /= pivot

        # ทำให้ทั้งคอลัมน์เป็น 0
        for i in range(n):
            if i != k:
                factor = A[i][k]
                for j in range(m):
                    A[i][j] -= factor * A[k][j]

    # ===== ตรวจผลลัพธ์ =====
    rank = 0
    for i in range(n):
        if any(abs(A[i][j]) > 1e-10 for j in range(n)):
            rank += 1
        elif abs(A[i][n]) > 1e-10:
            return "No solution"

    if rank < n:
        return "Infinite solutions"

    return [A[i][n] for i in range(n)]


# ===== Main Program =====
import copy

n = int(input("Enter number of variables: "))

A = []

print("Enter augmented matrix row by row:")
for _ in range(n):
    row = list(map(float, input().split()))
    A.append(row)

print("\nChoose method:")
print("1 = Gaussian Elimination")
print("2 = Gauss-Jordan")
choice = input("Enter choice: ")

# ใช้ copy เพื่อไม่ให้เมทริกซ์โดนแก้ซ้ำ
if choice == "1":
    result = gaussian_elimination(copy.deepcopy(A))
elif choice == "2":
    result = gauss_jordan(copy.deepcopy(A))
else:
    result = "Invalid choice"

print("\nResult:", result)