#include <stdio.h>

// ฟังก์ชันรับค่า a, b และรับ "แผนที่" ของผลลัพธ์ 2 ใบ (*sum, *diff)
void getSumAndDiff(int a, int b, int *sumResult, int *diffResult) {
    // 1. คำนวณบวก แล้วเอาไปใส่ในที่อยู่ที่ระบุไว้ใน sumResult
    *sumResult = a + b;

    // 2. คำนวณลบ แล้วเอาไปใส่ในที่อยู่ที่ระบุไว้ใน diffResult
    *diffResult = a - b;
}

int main() {
    int a = 10, b = 4;
    
    // ประกาศกล่องเปล่าๆ มารอรับค่า
    int mySum, myDiff;

    // ส่ง a, b ปกติ
    // แต่ส่ง &mySum, &myDiff (ส่งที่อยู่) ไปให้ pointer ข้างบน
    getSumAndDiff(a, b, &mySum, &myDiff);

    printf("Sum = %d, Diff = %d\n", mySum, myDiff);

    return 0;
}