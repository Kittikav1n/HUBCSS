#include<stdio.h>
int main(){
    int score;
    scanf("%d",&score);
    if (score >= 80){
        printf("Grade A");
    }
    else if (score < 80 && score >= 70 ){
        printf("Grade B");
    } 
    else if (score < 70 && score >= 60 ){
        printf("Grade C");
    }
    else if (score < 60 && score >= 50 ){
        printf("Grade D");
    }
    else{
        printf("Grade F");
    }
}