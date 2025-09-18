#include <stdio.h>

int main() {
    int R, C;

    if (scanf("%d %d", &R, &C) != 2) {
        return 1;
    }

    int matrix[R][C];
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (scanf("%d", &matrix[i][j]) != 1) {
                return 1;
            }
        }
    }
    printf("-----\n");
    for (int j = 0; j < C; j++) { 
        for (int i = 0; i < R; i++) { 
            printf("%d", matrix[i][j]);
            if (i < R - 1) {
                printf(" ");
            }
        }
        printf("\n");
    }
    printf("-----");
    return 0;
}