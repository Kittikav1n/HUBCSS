#include<stdio.h>
int main(){
    int n, i;
    int nums[100];
    printf("input: ");
    scanf("%d", &n);
    for(i = 0; i < n; i++){
        scanf("%d", (nums + i));
    }
    for(i = 0; i < n; i++){
        printf("number is %d address is%p\n",nums[i], (nums + i));
    }
    int *start = nums;
    int *end = nums + n - 1;
    int temp;
    while(start < end){
        temp = *start;
        *start = *end;
        *end = temp;
        *start++;
        *end--;
    }
    
    for(i = 0; i < n;i++){
        printf("%d ", *(nums+i));
    }
}

/*
input: 5

1 2 3 4 5

number is 1 address is0x7ffe01e79880
number is 2 address is0x7ffe01e79884
number is 3 address is0x7ffe01e79888
number is 4 address is0x7ffe01e7988c
number is 5 address is0x7ffe01e79890

5 4 3 2 1 
*/

