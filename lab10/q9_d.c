#include<stdio.h>
#include<stdlib.h>
/*
int main(void){
   float inM[8]={1.0,2.0,3.0,4.0,-1.0,-2.0,-3.0,-4.0};
   float *outM=NULL; 
   int r;
   int i; 
   r = fil(inM,2,4,&outM);
   for (i=0; i<8; i++){
      printf("%f\n",outM[i]);
   }
}
*/
int fil(float *matrixIn, int rows, int cols, float **matrixOut){
   int r;
   int c; 
   if (matrixOut == NULL){
      return -1;
   }
   (*matrixOut) = (float *)malloc(rows*cols*sizeof(float));
   if ((*matrixOut)==NULL){
      return -1;
   }
   for (r=0; r<rows; r++){
      for (c=0; c<cols; c++){
         if (matrixIn[r*cols+c]<0){
            (*matrixOut)[r*cols+c] = 0;
            printf("first");
         } else {
            printf("hi");
            (*matrixOut)[r*cols+c]= matrixIn[r*cols+c];
         }
      }
   }
   return 0;
}
