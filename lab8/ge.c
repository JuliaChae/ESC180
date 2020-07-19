#include<stdio.h>

int ge_fw(float *matrix, int rows, int cols, float *matrix_out){
   int i, row, col, temp;
   float factor;
   int startR =0;
   int startC=0;
   if (matrix == NULL||matrix_out==NULL){
      return -1;
   }
   for (row=0; row<rows; row++){
      for (col=0; col<cols; col++){
         matrix_out[row*cols + col] = matrix[row*cols+col];
      }
   }
   for (i = 0; i<rows; i++){
      if (matrix_out[startR*cols+startC]==0){
         for (row =startR; row<rows; row++){
            if (matrix_out[row*cols+startC] != 0){
               for (col = startC; col<cols;col++){
                  temp = matrix_out[row*cols+col];
                  matrix_out[row*cols+col] = matrix_out[startR*cols +col];
                  matrix_out[startR*cols+col]=matrix_out[row*cols+col];
               }   
            }
         }
      }
      for (row=startR+1; row<rows; row++){
         if (matrix_out[row*cols+startC]!=0){
            factor = matrix_out[row*cols+startC]/matrix_out[startR*cols+startC];
            for (col=startC;col<cols;col++){
               matrix_out[row*cols+col]=matrix_out[row*cols+col]-factor*matrix_out[startR*cols+col];
           }
         }
      }
      startR = startR+1;
      startC = startC+1;
   }
   return 0;
}

int ge_bw(float *matrix, int rows, int cols, float *matrix_out){
   int i, row, col, nonzeroi;
   int endR=rows;
   float nonzero, factor;
   if (matrix == NULL||matrix_out==NULL){
      return -1;
   }
   for (row=0; row<rows; row++){
      for (col=0; col<cols; col++){
         matrix_out[row*cols + col] = matrix[row*cols+col];
      }
   }
   for (i=0;i<rows;i++){
      for (col = 0; col<cols; col++){
         if (matrix_out[(endR-1)*cols+col]!=0){
            nonzero = matrix_out[(endR-1)*cols+col];
            nonzeroi = col;
            break;
         }
      }
      for (col=0; col<cols; col++){
         matrix_out[(endR-1)*cols+col]=matrix_out[(endR-1)*cols+col]/nonzero;
      }
     for (row=0;row<endR-1;row++){
         factor = matrix_out[row*cols+nonzeroi]/matrix_out[(endR-1)*cols+nonzeroi];
         for (col=0; col<cols; col++){
            matrix_out[row*cols+col]=matrix_out[row*cols+col]-factor*matrix_out[(endR-1)*cols+col];
         }
      }
      endR=endR-1;
   }  
   return 0; 
}
