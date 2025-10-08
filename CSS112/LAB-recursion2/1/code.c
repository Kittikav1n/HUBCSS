#include <stdio.h>
int max(int number[], int n ){
    if( n == 1) return number[0];
    int maxstep = max(number, n-1);
    if(number[n-1] > maxstep){
      return number[n-1];  
    } 
    else{
        return maxstep;
    }
    
}
int main()
{
    int n;
    scanf("%d", &n);
    int allnumber[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &allnumber[i]);
    }
    int maxtotal = max(allnumber, n);
    printf("%d",maxtotal);
    return 0;
}