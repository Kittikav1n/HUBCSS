//single_num
#include<stdio.h>
int sigle_num(int arr[], int num){
    int result = 0;
    for(int i=0; i<num; i++){
        result ^= arr[i];
    }
    return result;
}
int main(){
    int arr1[] ={2, 2, 1};
    int arr2[] = {4, 1, 2, 1, 2};
    int arr3[] = {1};
    printf("%d \n",sigle_num(arr1, 3));
    printf("%d \n",sigle_num(arr2, 5));
    printf("%d \n",sigle_num(arr3, 1));

}