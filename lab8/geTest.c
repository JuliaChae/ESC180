#include<stdio.h>
#include"ge.c"
int ge_fw(float *matrix, int rows, int cols, float *matrix_out);
int ge_bw(float *matrix, int rows, int cols, float *matrix_out);

int main(void){
   float matrix[3][4] = {{-3.0,2.0,-6.0,6.0},{5.0,7.0,-5.0,6.0},{1.0,4.0,-2.0,8.0}};
   float matrix_out[3][4];
   int i, x;
   ge_fw((float*)matrix, 3, 4, (float*)matrix_out);
   /*for (i =0; i<3; i++){
      for (x = 0; x<4; x++){
         printf("%f ",matrix[i][x]);
      }
   }*/ 
   for (i =0; i<3; i++){
      for (x = 0; x<4; x++){
         matrix[i][x]=matrix_out[i][x];
         /*printf("%f ",matrix_out[i][x]);*/
      }
   } 
   ge_bw((float*)matrix,3,4,(float*)matrix_out); 
   for (i =0; i<3; i++){
      for (x = 0; x<4; x++){
         printf("%f ",matrix_out[i][x]);
      }
   }
}

