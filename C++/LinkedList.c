#include<stdio.h>
#include<stdlib.h>
typedef struct Node{
    int No;
    int a;
    int b;
    int c;
    struct Node* next;
} Node;
Node* createNode(int No, int a, int b, int c){
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->No = No;
    newNode->a = a;
    newNode->b = b;
    newNode->c = c;
    newNode->next = NULL;
    return newNode;
}
int main(){
    Node* head = createNode(1, 1, 1, 1);
    head -> next = createNode(2, 2, 2, 2);
    head -> next -> next = createNode(3, 3, 3, 3);
    printf("No\ta\tb\tc\n");
    printf("-----------------------\n");
    printf("%d\t%d\t%d\t%d\n", head->No, head->a, head->b, head->c);
    head = head -> next;
    printf("%d\t%d\t%d\t%d\n", head->No, head->a, head->b, head->c);
    head = head -> next;
    printf("%d\t%d\t%d\t%d\n", head->No, head->a, head->b, head->c);
    return 0;
}
