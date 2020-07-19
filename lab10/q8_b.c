#include <stdio.h>

typedef struct {
   float *coef; 
   int *pow; 
   int len; 
} multipoly;
/*
int main(void){
   int p[4] = {3,2,4,5};
   float c[4] = {2.0, 5.0, 2.0, 10};
   int r;
   int i;
   multipoly poly;
   poly.coef = c;
   poly.pow = p;
   poly.len = 4; 
   r = integrate(&poly);
   printf("%d",r);
   for (i=0; i<4; i++){
      printf("%f\n", (poly.coef)[i]);
      printf("%d\n", (poly.pow)[i]);
   }
}
*/
int integrate(multipoly *poly){
   int i;
   if (poly ==NULL){
      return -1;
   } 
   for (i=0;i<(poly->len);i++){
      if ((poly->pow) ==-1){
         return -1;
      }
      (poly->coef)[i]= ((poly->coef)[i])*(1.0/((poly->pow)[i]+1)); 
      (poly->pow)[i] = (poly->pow)[i]+1;
   }
   return 0;
}
