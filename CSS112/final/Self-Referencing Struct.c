#include<stdio.h>
struct Node{
    int data;
    struct Node *next;
};
int main(){
    struct Node a, b;
    struct Node *p;
    a.data = 10;
    b.data = 20;
    a.next = &b;
    b.next = NULL;
    p = &a;
    printf("%d\n", p->data);
    printf("%d\n", p->next->data);
    
    printf("%p\n", &p->data);
    printf("%p\n", &p->next->data);
    return 0;
}