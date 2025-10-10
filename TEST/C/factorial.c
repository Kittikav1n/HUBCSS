//factorial
#include<stdio.h>
int factorial(int n){
    int total = 1;
    for(int i = n; i >= 1 ; i--){
        total *= i;
    }
    return total;
    
}

int main() {
    printf("Factorial of 5 is: %d\n", factorial(5));
    printf("Factorial of 0 is: %d\n", factorial(0));
    printf("Factorial of 7 is: %d\n", factorial(7));
    printf("Factorial of 1 is: %d\n", factorial(1));

    return 0;
}