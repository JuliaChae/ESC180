#include <stdio.h>

float bsqrt(float x, float tol);
float myAbs(float x);

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
