#include <stdio.h>
#include <stdlib.h> // สำคัญมากสำหรับ malloc, realloc, free

int main() {
    int capacity = 2; // ความจุเริ่มต้น (ตามโจทย์)
    int count = 0;    // จำนวนของที่มีอยู่จริง
    int input;

    // 1. จองพื้นที่เริ่มต้น
    int *arr = (int*) malloc(capacity * sizeof(int));

    // เช็คความปลอดภัย
    if (arr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    printf("Start input (type -1 to stop):\n");

    while (1) {
        // 2. รับค่า
        scanf("%d", &input);

        // 3. เงื่อนไขหยุด (ถ้าเจอ -1 ให้กระโดดออกจาก Loop ทันที)
        if (input == -1) {
            break;
        }

        // 4. เช็คว่า "เต็มหรือยัง?"
        if (count == capacity) {
            // 4.1 คำนวณขนาดใหม่ (เพิ่มทีละ 2)
            capacity += 2; 
            
            // 4.2 สั่งขยายพื้นที่ด้วย realloc
            // (ใช้ temp มารับก่อน เพื่อกันเหนียวเผื่อขยายไม่สำเร็จ ของเก่าจะได้ไม่หาย)
            int *temp = (int*) realloc(arr, capacity * sizeof(int));
            
            if (temp == NULL) {
                printf("Resizing failed!\n");
                free(arr); // คืนของเก่าก่อนตาย
                return 1;
            }
            
            // ถ้าสำเร็จ ให้ arr ชี้ไปที่ใหม่
            arr = temp;
            printf("--- Resized to %d slots ---\n", capacity);
        }

        // 5. เก็บข้อมูลลง Array
        arr[count] = input;
        count++; // นับจำนวนเพิ่ม
    }

    // 6. แสดงผล
    printf("\nNumbers: ");
    for (int i = 0; i < count; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    printf("Total Capacity: %d\n", capacity);
    printf("Count: %d\n", count);

    // 7. คืนพื้นที่ทั้งหมด
    free(arr);

    return 0;
}