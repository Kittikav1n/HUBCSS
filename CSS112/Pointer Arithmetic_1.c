#include <stdio.h>
#define COUNT 4

int main() {
    int *p;
    int a[COUNT]; // สร้างอาร์เรย์ขนาด 4 ช่อง

    printf("size of an 'int' is %lu bytes\n", sizeof(int));

    // 1. กำหนดค่าเริ่มต้นให้อาร์เรย์: a = {0, 1, 2, 3}
    for (int i = 0; i < COUNT; i++) {
        a[i] = i;
    }

    // 2. ให้ p ชี้ไปที่จุดเริ่มต้น (a[0])
    p = a;
    printf("Start:      Address of p is %p, Value is %d\n", p, *p);

    // 3. บวก 1 (ขยับไป 1 ช่อง)
    p = p + 1;
    printf("p = p + 1:  Address of p is %p, Value is %d\n", p, *p);

    // 4. บวกเพิ่มอีก 2 (ขยับไปอีก 2 ช่อง)
    p = p + 2;
    printf("p = p + 2:  Address of p is %p, Value is %d\n", p, *p);

    // 5. ลองของ: ขยับเลยขอบเขตอาร์เรย์ (Out of bounds)
    p = p + 1;
    printf("Beyond End: Address of p is %p, Value is %d (Garbage)\n", p, *p);

    return 0;
}
/*
OUTPUT
size of an 'int' is 4 bytes
Start:      Address of p is 0061FF00, Value is 0
p = p + 1:  Address of p is 0061FF04, Value is 1
p = p + 2:  Address of p is 0061FF0C, Value is 3
Beyond End: Address of p is 0061FF10, Value is 6422356 (Garbage)
*/