#include <stdio.h>
float numavg(float *array, int len);
/*
int main(void) {
   float r;
   float b[10] = {1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0};
   r = numavg(b,10);
   printf("%f",r);
}*/

float numavg(float *array, int len){
   int i;
   float sum =0;   

   if (array ==NULL){
      return -1.0;
   }
   for (i=0; i<len; i++){
      sum = sum + array[i];  
   }
   return sum/len; 
}
