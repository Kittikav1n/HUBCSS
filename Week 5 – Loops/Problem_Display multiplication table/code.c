#include<stdio.h>
int main(){
    int num,sum,i;
    scanf("%d",&num);
    for(i=1;i<=12;i++){
        sum = num*i;
        printf("%d x %d = %d\n",num,i,sum);
    }
    return 0;
}