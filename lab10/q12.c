#include<stdio.h>

typedef struct {
   int valid; 
   int value;
   int frequency; 
} array; 
/*
int main(void){
   int n[10] = {1,2,3,1,2,3,2,2,3,7};
   array m[10];
   int i;
   for (i=0;i<10;i++){
      m[i].valid = 0;
      m[i].value =0;
      m[i].frequency =0;
   }
   histogram(n,m,10);
   for (i=0;i<10;i++){
      printf("Frequency of %d is %d \n", m[i].value, m[i].frequency);
   }
   
}*/

int histogram(int *n, array *m, int s){
   int i, j;
   for (i=0; i<s; i++){
      for (j=0; j<s; j++){
         if (m[j].value ==n[i]){
            m[j].frequency+=1;
            break;
         } 
         else {
            if (m[j].valid ==0){
               m[j].value = n[i];
               m[j].valid = 1;
               m[j].frequency = 1;
               break;
            }
         }
      }
   }
}
 
