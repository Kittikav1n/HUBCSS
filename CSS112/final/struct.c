#include<stdio.h>
struct student{
    int id;
    float gpa;
};
int main(){
    struct student s1;
    struct student *Ps1;
    s1.id = 403;
    s1.gpa = 4.00;
    Ps1 = &s1;
    (*Ps1).id = 402;
    Ps1->gpa = 3.00;
    printf("%d\n", s1.id);
    printf("%.2f\n", s1.gpa);
    return 0;
}