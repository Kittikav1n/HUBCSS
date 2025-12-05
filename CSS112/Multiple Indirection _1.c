c#include <stdio.h>
#define LENGTH 3

int data[LENGTH]; // อาร์เรย์ขนาด 3 ช่อง

int main(int argc, char **argv) {
    int *pi;    // Pointer ชั้นเดียว (ชี้ไปที่ int)
    int **ppi;  // Pointer สองชั้น (ชี้ไปที่ Pointer อีกที)

    printf("multiple indirection example\n");

    // 1. วนลูปกำหนดค่าให้ array: data = {0, 1, 2}
    for (int i = 0; i < LENGTH; i++) {
        data[i] = i; 
    }

    // 2. วนลูปแสดงค่าใน array แบบปกติ
    for (int i = 0; i < LENGTH; i++) {
        printf("%d\n", data[i]);
    }

    // 3. เริ่มต้นการเชื่อมโยง Pointer
    pi = data;  // pi ชี้ไปที่หัวแถวของ array data
    ppi = &pi;  // ppi ชี้ไปที่ตัวแปร pi (เก็บ Address ของ pi)

    // 4. วนลูปเพื่อแสดงผลผ่าน Pointer หลายชั้น
    for (int i = 0; i < LENGTH; i++) {
        printf("array address is %p\n", data);
        printf("item pointed to by pi is %d\n", *pi);
        printf("item pointed to by ppi is %p\n", *ppi);
        printf("item pointed to by double indirection of ppi is %d\n\n", **ppi);
        
        printf("The address of pi is %p and the value of ppi (what it points to) is %p\n\n", &pi, ppi);

        pi += 1; // ขยับ pi ไปชี้สมาชิกตัวถัดไปใน array
    }
    return 0;
}
/*
OUTPUT
multiple indirection example
0
1
2
array address is 00408000
item pointed to by pi is 0
item pointed to by ppi is 00408000
item pointed to by double indirection of ppi is 0

The address of pi is 0060FE00 and the value of ppi (what it points to) is 0060FE00

array address is 00408000
item pointed to by pi is 1
item pointed to by ppi is 00408004  <-- สังเกตว่าค่าตรงนี้เปลี่ยน (เพราะ pi ขยับ)
item pointed to by double indirection of ppi is 1

The address of pi is 0060FE00 and the value of ppi (what it points to) is 0060FE00  <-- แต่ตรงนี้ไม่เปลี่ยน

... (ทำซ้ำสำหรับเลข 2) ...
*/