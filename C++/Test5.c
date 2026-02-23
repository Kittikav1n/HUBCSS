#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX 10;
typedef struct {
    char name[50];
    int score;
    struct Node* prev;
    struct Node* next;
} Node;
Node* createNode(const char* name, int score){
    Node* newNode = (Node*)malloc(sizeof(Node));
    strcpy(newNode->name, name);
    newNode->score = score;
    newNode->prev = NULL;
    newNode->next = NULL;
    return newNode;
}
void insertScore(Node** head_ref, char* name, int score){
    Node* newNode = createNode(name, score);
    Node* current;
    if(*head_ref == NULL || (*head_ref)->score < score){
        newNode->next = *head_ref;
        if(*head_ref != NULL){
            head_ref->prev = newNode;
        }        
        *head_ref = newNode;
    }
    
}
int main(){

}