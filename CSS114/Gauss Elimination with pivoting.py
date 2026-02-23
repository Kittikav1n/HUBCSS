import numpy as np

def gauss_elimination_pivoting(A, b):

    n = len(b)
    A = A.astype(float)
    b = b.astype(float)
    M = np.column_stack((A, b))
    
    # --- Forward Elimination ---
    for k in range(n):
        pivot_index = np.argmax(np.abs(M[k:n, k])) + k
        
        if pivot_index != k:
            M[[k, pivot_index]] = M[[pivot_index, k]]
            
        if np.abs(M[k, k]) < 1e-10:
            raise ValueError("Matrix is singular (ไม่สามารถหาคำตอบได้)")
            
        for i in range(k + 1, n):
            factor = M[i, k] / M[k, k]
            M[i, k:] -= factor * M[k, k:]
            
    # --- Back Substitution ---
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum_ax = np.sum(M[i, i+1:n] * x[i+1:n])
        x[i] = (M[i, n] - sum_ax) / M[i, i]
        
    return x

def get_input_from_terminal():
    print("=== โปรแกรมแก้สมการเชิงเส้น (Gauss Elimination) ===")
    
    while True:
        try:
            # 1. รับขนาดเมทริกซ์
            n_input = input("ป้อนจำนวนตัวแปร (N): ")
            if not n_input.strip(): continue # ป้องกันกด Enter ว่างๆ
            n = int(n_input)
            break
        except ValueError:
            print("❌ กรุณาป้อนตัวเลขจำนวนเต็มเท่านั้น")

    print(f"\n--- กรุณาป้อนสัมประสิทธิ์ Matrix A ({n}x{n}) ---")
    print("ตัวอย่าง: ถ้าสมการคือ 2x + 1y = 5 ให้พิมพ์: 2 1")
    
    matrix_a = []
    for i in range(n):
        while True:
            try:
                # รับค่าทีละแถว แยกด้วยเว้นวรรค
                row_str = input(f"แถวที่ {i+1}: ")
                row_vals = list(map(float, row_str.split()))
                
                # เช็คว่าป้อนครบจำนวนไหม
                if len(row_vals) != n:
                    print(f"❌ คุณป้อนมา {len(row_vals)} ตัว (ต้องการ {n} ตัว) กรุณาป้อนใหม่")
                    continue
                    
                matrix_a.append(row_vals)
                break
            except ValueError:
                print("❌ รูปแบบไม่ถูกต้อง กรุณาป้อนตัวเลขเว้นวรรค เช่น: 1 2 3")

    print(f"\n--- กรุณาป้อนเวกเตอร์คำตอบ b ({n} ตัว) ---")
    print("ตัวอย่าง: ถ้าคำตอบคือ 5, -2, 9 ให้พิมพ์: 5 -2 9")
    
    while True:
        try:
            b_str = input(f"ค่าคงที่ b: ")
            b_vals = list(map(float, b_str.split()))
            
            if len(b_vals) != n:
                 print(f"❌ คุณป้อนมา {len(b_vals)} ตัว (ต้องการ {n} ตัว) กรุณาป้อนใหม่")
                 continue
            
            break
        except ValueError:
            print("❌ รูปแบบไม่ถูกต้อง")

    return np.array(matrix_a), np.array(b_vals)

# --- Main Execution ---
if __name__ == "__main__":
    try:
        # เรียกฟังก์ชันรับค่า
        A_input, b_input = get_input_from_terminal()
        
        print("\n" + "="*30)
        print("กำลังประมวลผล...")
        solution = gauss_elimination_pivoting(A_input, b_input)
        
        print(f"✅ คำตอบของระบบสมการคือ:")
        for i, val in enumerate(solution):
            print(f"x_{i+1} = {val:.4f}")
        print("="*30)
        
    except ValueError as e:
        print(f"\n❌ Error: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")