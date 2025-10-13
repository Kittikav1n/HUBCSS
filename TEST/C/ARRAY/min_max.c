#include<stdio.h>
int find_max(int arr[], int size){
    int maxval = arr[0];
    for(int i = 0 ; i < size ; i++){
        if(maxval < arr[i]){
            maxval = arr[i];
            
        }
    }
    return maxval;
}
int find_min(int arr[], int size){
    int minval = arr[0];
    for(int i = 0 ; i < size ; i++){
        if(minval > arr[i]){
            minval = arr[i];
        }
    }
    return minval;
}
int main(){
    int arr1[] = {1, 2, 3};
    printf("MAX: %d\n", find_max(arr1,3));
    printf("MIN: %d\n", find_min(arr1,3));
    return 0;
}