#include <stdio.h>

double calculate_average(int arr[], int n) {
    int sum = 0;
    for(int i = 0; i < n; i++){
        sum += arr[i] ; 
    }
    double sum2 = (double)sum/n;
    return sum2;
}

int main() {
    // --- เทสเคส ---
    int arr1[] = {1, 2, 3, 4, 5};
    printf("ค่าเฉลี่ยคือ: %.2f\n", calculate_average(arr1, 5));

    int arr2[] = {10, 20, 30};
    printf("ค่าเฉลี่ยคือ: %.2f\n", calculate_average(arr2, 3));

    int arr3[] = {1, 1, 1, 1, 2};
    printf("ค่าเฉลี่ยคือ: %.2f\n", calculate_average(arr3, 5));

    int arr4[] = {15};
    printf("ค่าเฉลี่ยคือ: %.2f\n", calculate_average(arr4, 1));

    return 0;
}