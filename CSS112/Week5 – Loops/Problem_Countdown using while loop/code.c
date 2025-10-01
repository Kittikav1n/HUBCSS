#include<stdio.h>
int main(){
    int num,i;
    scanf("%d",&num); 
    i = num;
    while(i > 0){
        printf("%d \n",i);
        i--;
    }
    return 0;
}