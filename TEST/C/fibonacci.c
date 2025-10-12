#include<stdio.h>
void fibo(int num){
    int a = 0, b = 1;
    printf("%d ", a);
    for(int i=2; i<= num; i++){
        int next = a + b;
        a = b;
        b = next;
        printf("%d ", b);
    }
}
int main(){
    fibo(5);
    printf("\n");
    fibo(10);
}