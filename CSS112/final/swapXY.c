#include<stdio.h>
void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
int main(){
    int x, y;
    printf("input x: ");
    scanf("%d", &x);
    printf("input Y: ");
    scanf("%d", &y);
    printf("x = %d, y = %d\n", x, y);
    swap(&x, &y);
    printf("x = %d, y = %d", x, y);
    return 0 ;
    
}