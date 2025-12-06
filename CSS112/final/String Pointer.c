#include<stdio.h>
#include<ctype.h>
int main(){
    char str[100];
    printf("INPUT: ");
    scanf("%s", str);
    char *Pstr = str;
    int length = 0, vowels = 0;
    char c;
    while(*Pstr != '\0'){
        c = tolower(*Pstr);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            vowels++ ;
        }
        length++;
        Pstr++;
    }
    printf("Length: %d\n", length);
    printf("Vowels: %d\n", vowels);
    return 0;
}