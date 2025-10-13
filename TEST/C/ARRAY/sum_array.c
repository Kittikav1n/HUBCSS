#include<stdio.h>
int find_sum(int arr[], int size){
    int total = 0;
    for(int i = 0; i < size; i++ ){
        total += arr[i];
    }
    return total;
}
int main(){
    int arr1[] = {1, 2, 3};
    int arr2[] = {2, 3, 4, 5};
    printf("Total: %d\n", find_sum(arr1, 3));
    printf("Total: %d\n",find_sum(arr2, 4));
    return 0;
}