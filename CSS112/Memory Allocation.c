#include <stdio.h>
#include <stdlib.h> // จำเป็นสำหรับ malloc, free
#include <string.h> // จำเป็นสำหรับ strncpy

int main() {
    char *s;
    int stringsize;

    // 1. คำนวณขนาดที่ต้องการ ("hello" มี 5 ตัว + \0 อีก 1 ตัว = 6 bytes)
    stringsize = sizeof("hello");
    printf("size of 'hello' is %d\n", stringsize);

    // 2. ขอจองพื้นที่ใน Heap (malloc)
    // ต้องแปลงร่าง (cast) เป็น (char*) เพราะ malloc ส่งคืน void*
    s = (char*)malloc(stringsize);

    // 3. ตรวจสอบความปลอดภัย: ถ้าแรมเต็ม malloc จะคืนค่า NULL
    if (s == NULL) {
        printf("malloc failed!\n");
        exit(0);
    }

    // 4. ลองปริ้นท์ทันทีหลังจอง (ในเมมโมรี่ตอนนี้จะเป็นค่าขยะ)
    // หมายเหตุ: อาจจะเห็นหรือไม่เห็นอะไรเลยก็ได้ ขึ้นอยู่กับดวง
    printf("1. s is now.. %s\n", s);

    // 5. เอาข้อความใส่ลงไปในพื้นที่ที่จองไว้
    strncpy(s, "hello", stringsize);
    printf("2. s is now %s\n", s);

    // 6. แก้ไขข้อมูลใน Heap (เปลี่ยน 'h' เป็น 'c')
    s[0] = 'c';
    printf("3. s is now %s\n", s);

    // 7. คืนพื้นที่ (Free) - สำคัญมาก!
    free(s);

    // 8. !!! จุดอันตราย (Undefined Behavior) !!!
    // โค้ดต้นฉบับพยายามปริ้นท์ s หลังจากคืนพื้นที่ไปแล้ว
    // ผลลัพธ์คาดเดาไม่ได้ (อาจจะเจอค่าเดิม, ค่ามั่ว, หรือโปรแกรมพัง)
    printf("4. s is now %s\n", s);

    return 0;
}


/*
OUTPUT
size of 'hello' is 6
1. s is now.. (อาจเป็นค่าว่าง หรือตัวอักษรขยะ)
2. s is now hello
3. s is now cello
4. s is now cello (หรือค่าขยะ หรือ Error)
*/
