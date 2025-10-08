#include <stdio.h>
    struct student{
        char name[30];
        int age;
        float grade;
    };
    float sum = 0;
    
struct student max(struct student students[], int n) {
    struct student max_s = students[0];
    for (int i = 1; i < n; i++) {
        if (students[i].grade > max_s.grade) {
            max_s = students[i];
        }
    }
    return max_s;
}


void outdata(struct student students[], int n){
    for (int i = 0; i <5 ; i++){
        printf("Name %s Age %d Grade %.2f \n", students[i].name, students[i].age, students[i].grade);
    }
}

int main()
{
    struct student students[5];
    for (int i = 0; i < 5; i++){
        scanf("%29s %d %f", students[i].name, &students[i].age, &students[i].grade);
        sum  += students[i].grade;  
    }
    struct student maxscore = max(students, 5);
    outdata(students, 5);
    printf("Grade point average: %.2f\n",sum / 5);
    printf("Max score student: Name %s Age %d Grade %.2f\n", maxscore.name, maxscore.age, maxscore.grade);
    return 0;
}
