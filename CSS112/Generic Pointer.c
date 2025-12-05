#include <stdio.h>
#define LENGTH 3

int data[LENGTH];       // อาร์เรย์เก็บตัวเลข
char *words[LENGTH];    // อาร์เรย์เก็บข้อความ (Pointer to strings)

int main(int argc, char **argv) {
    void *gp; // พระเอกของเรา: Generic Pointer (ชี้อะไรก็ได้)

    printf("generic pointer example\n");

    // --- ส่วนเตรียมข้อมูล (Initialization) ---
    // 1. ใส่เลข 0, 1, 2 ลงใน data
    for (int i = 0; i < LENGTH; i++) {
        data[i] = i;
        printf("%d\n", data[i]); // ปริ้นท์เลขออกมาดู
    }

    // 2. ใส่คำว่า "zero", "one", "two" ลงใน words
    words[0] = "zero";
    words[1] = "one";
    words[2] = "two";
    for (int i = 0; i < LENGTH; i++) {
        printf("%s\n", words[i]); // ปริ้นท์คำออกมาดู
    }

    // --- ส่วนทดสอบ Generic Pointer ---
    
    // กรณีที่ 1: ชี้ไปที่ Integer Array
    gp = data; // ให้ gp ชี้ไปที่จุดเริ่มต้นของ array data [cite: 165]
    
    printf("\ndata array address is %p\n", gp); // [cite: 166-168]
    
    // *gp เฉยๆ ทำไม่ได้ ต้องแปลงร่างเป็น (int*) ก่อนค่อยดึงค่า (*)
    printf("item pointed to by gp is %d\n", *(int*)gp); // [cite: 169-171]

    // ขยับ Pointer: ต้องแปลงร่างเป็น (int*) ก่อนบวก เพื่อให้ขยับทีละ 4 bytes
    gp = (int*)gp + 1; // 
    printf("item pointed to by gp is now %d\n", *(int*)gp); // [cite: 173]

    // กรณีที่ 2: ชี้ไปที่ String Array
    gp = words; // ให้ gp ย้ายไปชี้ที่ array words [cite: 174]
    
    printf("\nwords array address is %p\n", gp); // [cite: 175-176]
    
    // words เก็บ pointer ดังนั้นต้องแปลงร่าง gp เป็น pointer ซ้อน pointer (char**)
    printf("item pointed to by gp is %s\n", *(char**)gp); // [cite: 177-178]

    // ขยับ Pointer: ต้องแปลงร่างเป็น (char**) ก่อนบวก
    gp = (char**)gp + 1; // 
    printf("item pointed to by gp is now %s\n", *(char**)gp); // [cite: 180]

    return 0;
}
/*
OUTPUT
generic pointer example
0
1
2
zero
one
two

data array address is 00408000
item pointed to by gp is 0
item pointed to by gp is now 1

words array address is 00408020
item pointed to by gp is zero
item pointed to by gp is now one
*/