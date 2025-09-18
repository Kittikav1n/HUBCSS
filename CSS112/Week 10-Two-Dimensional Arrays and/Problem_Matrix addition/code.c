#include <stdio.h>

int main() {
    int R, C;
    if (scanf("%d %d", &R, &C) != 2) {
        return 1;
    }

    int matrixA[R][C];
    int matrixB[R][C];
    int matrixC[R][C];

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (scanf("%d", &matrixA[i][j]) != 1) {
                return 1;
            }
        }
    }
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (scanf("%d", &matrixB[i][j]) != 1) {
                return 1;
            }
        }
    }

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            matrixC[i][j] = matrixA[i][j] + matrixB[i][j];
        }
    }
    printf("-----\n");
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            printf("%d ", matrixC[i][j]);
            if (j < C - 1) {
                printf(" ");
            }
        }
        printf("\n");
    }
    printf("-----");

    return 0;
}