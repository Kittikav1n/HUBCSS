#include<stdio.h>
#include<stdlib.h>
int main(){
    int n, i;
    int *arr;
    printf("INPUT:");
    scanf("%d", &n);
    arr = (int*) malloc (n*sizeof(int));//คำสั่งจองหน่วยความจำ
    if(arr == NULL){//ตรวจสอบการจองหน่วยความจำ
        return 1;
    }
    for(i=0;i<n;i++){
        scanf("%d", (arr + i));
    }
    for(i=n-1;i>=0;i--){
        printf("%d ", *(arr + i));
    }
    free(arr);//คำสั่งคืนหน่วยความจำ
    return 0;
}