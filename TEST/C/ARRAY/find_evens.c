#include<stdio.h>
void evens(int arr[], int size){
    int count = 0;
    for(int i = 0 ; i < size ; i++){
        if(arr[i] % 2 == 0){
            printf("%d ", arr[i]);
            count++;
        }
    }
    printf("\n");
    printf("total evens: %d", count) ;
}
int main(){
    int arr1[] = {1, 2, 3, 4};
    evens(arr1, 4);
}