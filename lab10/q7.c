#include <stdio.h>

int main(void){
   int *b;
   int **a;
   int c =10;
   int d=20;
   int q = 30;
   b = &c;
   a = &b;
   q = **a; 
   *b=0;
   d = c + 100;
   q = q+100; 
   printf("a is %d, b is %d, c is %d, d is %d, q is %d.", a,b,c,d,q);
   return 0;
}

/*
 * a is a pointer to b 
 * b is a pointer to c 
 * c is 0
 * d is 100
 * q is 110
 */
