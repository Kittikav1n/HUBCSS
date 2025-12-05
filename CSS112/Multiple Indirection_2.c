#include <stdio.h>
#define LENGTH 3

char *words[LENGTH]; // อาร์เรย์เก็บ Pointer (เก็บที่อยู่ของข้อความ)

int main(int argc, char **argv) {
    char *pc;   // Pointer ชั้นเดียว (เอาไว้ชี้ตัวอักษร)
    char **ppc; // Pointer สองชั้น (เอาไว้ชี้ไปที่ตัว Pointer ในอาร์เรย์ words)

    printf("multiple indirection example\n");

    // 1. กำหนดค่า: ให้แต่ละช่องของอาร์เรย์เก็บ Address ของข้อความ
    words[0] = "zero";
    words[1] = "one";
    words[2] = "two";

    // 2. ลูปแรก: ปริ้นท์แบบปกติ (ใช้ Array Index)
    for (int i = 0; i < LENGTH; i++) {
        printf("%s\n", words[i]);
    }

    // 3. ลูปที่สอง: ปริ้นท์โดยใช้ Pointer ซ้อน Pointer (Double Indirection)
    ppc = words; // ให้ ppc เริ่มต้นชี้ที่หัวแถวของอาร์เรย์ words
    for (int i = 0; i < LENGTH; i++) {
        // ขยับ ppc ไปที่ช่องที่ i ของอาร์เรย์ words
        ppc = words + i; 
        
        // *ppc คือการดึงค่าจากช่องนั้นมา (ซึ่งก็คือ Address ของคำว่า "zero"/"one"...)
        // เอา Address นั้นไปใส่ใน pc (Pointer ชั้นเดียว)
        pc = *ppc;

        // วนลูปย่อย: ปริ้นท์ทีละตัวอักษรจนกว่าจะเจอจุดจบสตริง (null terminator)
        while (*pc != 0) {
            printf("%c", *pc);
            pc += 1; // ขยับไปตัวอักษรตัวถัดไป (z -> e -> r -> o)
        }
        printf("\n"); // จบคำแล้วขึ้นบรรทัดใหม่
    }
    return 0;
}
/*
OUTPUT:
multiple indirection example
zero
one
two
zero
one
two
*/