#include <stdio.h>
#include <string.h>

void reverse_string (char *str){
    int l = 0 ;
    int r = strlen(str) - 1 ;
    char temp ;
    while (l < r){
        temp = str[r];
        str[r] = str[l];
        str[l] = temp ;
        r--;
        l++;
    }
}
int main() {
    char str1[] = "hello";
    reverse_string(str1);
    printf("Reversed string: %s\n", str1);

    char str2[] = "world";
    reverse_string(str2);
    printf("Reversed string: %s\n", str2);
    char str3[] = "a";
    reverse_string(str3);
    printf("Reversed string: %s\n", str3);
    char str4[] = "";
    reverse_string(str4);
    printf("Reversed string: %s\n", str4);
    return 0;
}