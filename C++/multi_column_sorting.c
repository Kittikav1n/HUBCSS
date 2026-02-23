#include<stdio.h>
#include<stdlib.h>
typedef struct {
    int No;
    int a;
    int b;
    int c;
} DataRow;
int compareRow(const void *p1, const void *p2){
    const DataRow *r1 = (const DataRow *)p1;
    const DataRow *r2 = (const DataRow *)p2;
    
    if(r1->a != r2->a){
        return r1->a - r2->a;
    }
    if(r1->b != r2->b){
        return r1->b - r2->b;
    }
    return r1->c - r2->c;
}
int insertData(DataRow arr[], int* n, DataRow newData){
    int i = *n - 1;
    while(i>=0 && compareRow(&arr[i], &newData) > 0){
        arr[i + 1] = arr[i];
        i--;
    }
    arr[i+1] = newData;
    (*n)++;
    return 0;
}

int main(){
    DataRow table[15] ={
        {1, 1, 1, 4}, {2, 3, 1, 1}, {3, 4, 4, 4}, {4, 2, 4, 4},
        {5, 3, 5, 3}, {6, 4, 3, 3}, {7, 1, 3, 3}, {8, 2, 4, 3},
        {9, 3, 3, 5}, {10, 1, 5, 3}, {11, 1, 1, 4}, {12, 4, 1, 1},
        {13, 5, 2, 3}, {14, 3, 5, 2}
    };
    DataRow Newitem = {99, 2, 4, 4};
    printf("insert data (No=%d, a=%d, b=%d, c=%d)\n", Newitem.No, Newitem.a, Newitem.b, Newitem.c);
    insertData(table, &(int){14}, Newitem);

    int n = sizeof(table) / sizeof(table[0]);
    qsort(table, n, sizeof(DataRow), compareRow);
    printf("No\ta\tb\tc\n");
    printf("-----------------------\n");
    for(int i = 0; i < n; i++){
        printf("%d\t%d\t%d\t%d\n", table[i].No, table[i].a, table[i].b, table[i].c);
    }    
}