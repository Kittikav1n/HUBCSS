#include<stdio.h>
int main(){
    int n, i;
    int nums[100];

    printf("input: ");
    scanf("%d", &n);
    //รับคค่า
    for(i = 0; i < n; i++){
        scanf("%d", (nums + i));//(nums + i) คือ การรับค่าแต่เอาแค่address
    }
    for(i = 0; i < n; i++){
        printf("number is %d address is%p\n",nums[i], (nums + i));
    }//nums[i] คือ การpintf ค่าทจำนวนnที่รับมา (nums + i) คือการprintf address ของค่าn
}
/*
input: 4
1
2
3
4
number is 1 address is0x7fff43426990
number is 2 address is0x7fff43426994
number is 3 address is0x7fff43426998
number is 4 address is0x7fff4342699c
*/ 