#include<stdio.h>
int fizzbuzz(){
    for(int i=1; i<=100; i++){
        if(i%3 && i%5 == 0){
            printf("FizzBuzz\n");
        }
        else if(i%5==0){
            printf("Buzz\n");
        }
        else if(i%3==0){
            printf("Fizz\n");
        }
        else{
            printf("%d\n", i);
        }
    }
}
int main(){
    fizzbuzz();
    return 0;
}