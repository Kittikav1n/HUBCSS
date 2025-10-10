#include <stdio.h>
#include <string.h>

void reverse_string (char *str){
    int l = 0 ;
    int r = strlen(str) - 1 ;
    char temp ;
    while (l < r){
        temp = str[r];
        str[r] = str[l];
        str[l] = temp ;
        r--;
        l++;
    }
}
int main() {
    char str1[] = "hello";
    reverse_string(str1);
    printf("Reversed string: %s\n", str1);

    char str2[] = "world";
    reverse_string(str2);
    printf("Reversed string: %s\n", str2);
    char str3[] = "a";
    reverse_string(str3);
    printf("Reversed string: %s\n", str3);
    char str4[] = "";
    reverse_string(str4);
    printf("Reversed string: %s\n", str4);
    return 0;
}



//max_min_in_array
#include <stdio.h>
int max(int arr[], int n){
    int maxval = arr[0];
    for (int i = 0; i < n; i++){
        if(maxval < arr[i]){
            maxval = arr[i];
        }
    }
    return maxval;
    
}
int min(int arr[], int n){
    int minval = arr[0];
    for (int i = 0; i < n; i++){
        if(minval > arr[i]){
            minval = arr[i];
        }
    }
    return minval;
}

int main(){
    int arr1[] = {1, 5, 3, 9, 2};
    printf("Max value is: %d\n", max(arr1, 5));
    printf("Min value is: %d\n", min(arr1, 5));
    printf("\n");
    int arr2[] = {-10, -5, -3, -9, -2};
    printf("Max value is: %d\n", max(arr2, 5));
    printf("Min value is: %d\n", min(arr2, 5));
    printf("\n");
    int arr3[] = {100};
    printf("Max value is: %d\n", max(arr3, 1));
    printf("Min value is: %d\n", min(arr3, 1));
    return 0;
}