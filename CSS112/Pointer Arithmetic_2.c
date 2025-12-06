#include <stdio.h>
#define COUNT 4

// ประกาศอาร์เรย์ของข้อมูลชนิดต่างๆ
int a[COUNT];
float b[COUNT];
double c[COUNT];
long long int d[COUNT];
short int e[COUNT];
long int f[COUNT];

int main() {
    // ประกาศ Pointer ให้ตรงกับชนิดข้อมูล
    int *pa;
    float *pb;
    double *pc;
    long long int *pd;
    short int *pe;
    long int *pf;

    // 1. แสดงขนาดของข้อมูลแต่ละชนิด (Size)
    printf("Sizes in bytes:\n");
    printf("int: %lu, float: %lu, double: %lu\n", sizeof(int), sizeof(float), sizeof(double));
    printf("long long: %lu, short: %lu, long: %lu\n\n", sizeof(long long int), sizeof(short int), sizeof(long int));

    // 2. ให้ Pointer ชี้ไปที่จุดเริ่มต้นของแต่ละอาร์เรย์
    pa = a; pb = b; pc = c;
    pd = d; pe = e; pf = f;

    // 3. กำหนดค่าข้อมูล (0, 1, 2, 3) ลงในทุกอาร์เรย์
    for (int i = 0; i < COUNT; i++) {
        a[i] = i;       b[i] = (float)i;
        c[i] = (double)i; d[i] = i;
        e[i] = i;       f[i] = i;
    }

    // 4. สั่งบวก Pointer เพิ่ม 1 (Pointer Arithmetic)
    // ตรงนี้แหละครับที่จะเห็นความต่าง!
    pa += 1; pb += 1; pc += 1;
    pd += 1; pe += 1; pf += 1;

    // 5. แสดงผลเปรียบเทียบ Address เริ่มต้น (Array) vs Address ปัจจุบัน (Pointer)
    printf("--- Results after adding 1 to pointer ---\n");
    
    // int: ควรขยับ 4 bytes
    printf("int:       Array @ %p, Pointer @ %p (Diff: %ld) -> Val: %d\n", a, pa, (char*)pa - (char*)a, *pa);
    
    // float: ควรขยับ 4 bytes
    printf("float:     Array @ %p, Pointer @ %p (Diff: %ld) -> Val: %.1f\n", b, pb, (char*)pb - (char*)b, *pb);
    
    // double: ควรขยับ 8 bytes
    printf("double:    Array @ %p, Pointer @ %p (Diff: %ld) -> Val: %.1f\n", c, pc, (char*)pc - (char*)c, *pc);
    
    // long long: ควรขยับ 8 bytes
    printf("long long: Array @ %p, Pointer @ %p (Diff: %ld) -> Val: %lld\n", d, pd, (char*)pd - (char*)d, *pd);
    
    // short: ควรขยับ 2 bytes
    printf("short:     Array @ %p, Pointer @ %p (Diff: %ld) -> Val: %d\n", e, pe, (char*)pe - (char*)e, *pe);

    return 0;
}

/*
OUTPUT
Sizes in bytes:
int: 4, float: 4, double: 8
long long: 8, short: 2, long: 4 (หรือ 8 ขึ้นอยู่กับ OS)

--- Results after adding 1 to pointer ---
int:       Array @ 00408000, Pointer @ 00408004 (Diff: 4) -> Val: 1
float:     Array @ 00408020, Pointer @ 00408024 (Diff: 4) -> Val: 1.0
double:    Array @ 00408040, Pointer @ 00408048 (Diff: 8) -> Val: 1.0
long long: Array @ 00408080, Pointer @ 00408088 (Diff: 8) -> Val: 1
short:     Array @ 004080C0, Pointer @ 004080C2 (Diff: 2) -> Val: 1
*/