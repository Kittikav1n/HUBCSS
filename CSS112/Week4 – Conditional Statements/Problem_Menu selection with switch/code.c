#include<stdio.h>
int main(){
    int chose;
    scanf("%d",&chose);
    switch(chose){
        case 1:
            printf("You chose Option 1\n");
            break;
        case 2:
            printf("You chose Option 2\n");
            break;
        case 3:
            printf("You chose Option 3\n");
            break;
        default:
            printf("Invalid choice");
    }
    return 0;
}