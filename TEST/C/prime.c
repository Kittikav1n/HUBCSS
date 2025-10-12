#include<stdio.h>
#include<stdbool.h>
int prime(int num){
    if(num<=1){
        return false;
    }
    else{
    for(int i = 2; i < num-1; i++){
        if(num % i == 0){
            return false;
        }
    }
    return true;
    }
}
int main(){
    int num1 = 1;
    if(prime(num1)){
        printf("True\n");
    }
    else{
        printf("False\n");
    }
    int num2 = 7;
    if(prime(num2)){
        printf("True\n");
    }
    else{
        printf("False\n");
    }
}