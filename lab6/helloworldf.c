#include <stdio.h>

float bsqrt(float x, float tol);
float myAbs(float x);

int main(void) {
   int i;
   for (i=0; i<10; i++){
      float sqrt;
      sqrt = bsqrt((float)i, 0.001);
      printf("The sqrt of %d is %f\n", i, sqrt);
   }
   return 0;
}

float bsqrt(float x, float tol) {
   float estimate = x/2; 
   while (myAbs(x-estimate*estimate)>tol){
      estimate = (estimate + x/estimate)/2;
   }
   return estimate;
}

float myAbs(float x){
   if (x>=0){
      return x;}
   else {
      return -x;}
}
