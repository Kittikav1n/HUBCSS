#include<stdio.h>
int main(){
    int arr[100];
    int n, Newnum, Oldnum;
    printf("INPUT: ");
    scanf("%d", &n);
    for(int i = 0; i  <  n;i++){
        scanf("%d", (arr + i));
    }
    printf("NEW NUMBER: ");
    scanf("%d", &Newnum);
    printf("OLD NUMBER: ");
    scanf("%d",&Oldnum);
    
    int *Pnum = arr;
    for(int i = 0;i < n;i++){
        if(*Pnum == Oldnum){
            *Pnum = Newnum;
        }
        Pnum++;
    }
    
    Pnum = arr;
    for(int i = 0; i < n; i++){
        printf("%d ", *Pnum);
        Pnum++;
    }
    return 0;
}