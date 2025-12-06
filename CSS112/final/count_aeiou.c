#include<stdio.h>
int main(){
    char str[100];
    printf("INPUT: ");
    scanf("%s", str);
    char *Pstr = str;
    int count = 0;
    while(*Pstr != '\0'){
        if(*Pstr == 'a' || *Pstr == 'e' || *Pstr == 'i' || *Pstr == 'o' || *Pstr == 'u'){
            cout++;
        }
        Pstr++;
        
    }
    printf("%d", count);
}