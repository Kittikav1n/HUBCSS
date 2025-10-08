#include <stdio.h>
#include <string.h>

int Palindrome(char str[], int start, int end) {
    
    if (start >= end) {
        return 1; // 1 หมายถึง true (เป็น Palindrome)
    }
    if (str[start] != str[end]) {
        return 0; // ถ้าไม่เหมือนกัน ก็ไม่ใช่ Palindrome แน่นอน
    }

    //ถ้าเหมือนกัน ให้เรียกฟังก์ชันเดิมซ้ำ แต่ขยับตำแหน่งเข้ามาตรงกลาง
    return Palindrome(str, start + 1, end - 1);
}

int main() {
    char text[100];
    printf("Enter Text: ");
    scanf("%s", text);    
    
    int len = strlen(text); 
    if (Palindrome(text, 0, len-1))
        printf("'%s' is a palindrome.\n", text);
    
    else {
        printf("'%s' is not a palindrome.\n", text);
    }
    return 0;
}