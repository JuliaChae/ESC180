#include<stdio.h>
#include<stdlib.h>
/*
int main(void){
   float a[10] = {1,2,3,4,5,6,7,8,9,10};
   float b[10] = {1,2,3,4,5,6,7,8,9,10};
   float *output; 
   int r;
   int i; 
   r = nsum(a,b,10,&output);
   for (i=0; i<10; i++){
      printf("%f\n", output[i]);
   }
}*/

int nsum(float *a, float *b, int len, float **out){
   int i; 
   if (a==NULL || b==NULL||out == NULL){
      return -1;
   } 
   (*out)=(float *)malloc(len*sizeof(float)); 
   if ((*out)==NULL){
      return -1;
   }
   for (i=0; i<len; i++){
      (*out)[i] = a[i]+b[i]; 
   } 
} 
