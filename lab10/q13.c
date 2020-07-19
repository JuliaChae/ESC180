#include<stdio.h>

typedef struct {
   int valid;
   int value;
   int frequency;
} array;

/*
int main(void){
   array m[10];
   int mode;
   int r; 
   r = getmode(m,&r); 
}*/

int getmode(array *m, int * mode){
   int mo;
   int count=0;
   if (m==NULL){
      return -1;
   }
   mo = m[0].frequency; 
   while(m[count].valid !=0){
      count = count + 1;
      if (m[count].frequency > mo){
         mo = m[count].frequency; 
      }
   }
   (*mode) = mo; 
   return 0;
}
