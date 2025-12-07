#include<stdio.h>
#include<stdlib.h>
int main(){
    int num, i;
    printf("INPUT NUM:");
    scanf("%d", &num);
    int *arr = (int*) malloc (num * sizeof(int));
    if(arr == NULL){
        return 0;
    }
    for(i=0;i<num;i++){
        scanf("%d", (arr + i));
    }
    int max = *arr;
    int min = *arr;
    for(i=0;i<num;i++){
        if(*(arr+i) > max){
            max = *(arr+i);
        }
        else if(*(arr+i) < min){
            min = *(arr+i);
        }
    }
    
    int range = max - min;
    printf("Max is %d\n",max);
    printf("Min is %d\n",min);
    printf("Range is %d",range);
    free(arr);
    return 0;
}
