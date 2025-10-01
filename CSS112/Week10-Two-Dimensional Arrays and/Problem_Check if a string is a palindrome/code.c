#include<stdio.h>
#include<string.h>
int main(){
    char word[101];
    scanf("%100s", word);
    int length = strlen(word);
    int palindrome = 1;
    for (int i = 0; i < length / 2; i++) {
        if (word[i] != word[length - 1 - i]) {
            palindrome = 0;
            break;
        }
    }
    if (palindrome) {
        printf("Palindrome\n");
    } else {
        printf("Not palindrome\n");
    }

    return 0;
}