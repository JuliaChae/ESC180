#include <stdio.h>
#include <stdlib.h>
/*
int main(void){
   int r;
   r = isPrime(23);
   printf("%d",r);
   r = isPrimeProduct(10);
   printf("%d",r);
} 
*/
int isPrime(int n){
   int i; 
   for (i=2; i<n; i++){
      if (n%i==0){
         return -1;
      }
   }
   return 0;                                                       
}

int isPrimeProduct(int n){
   int i;
   int j;
   int fact1;
   int fact2; 
   for (i=0; i<n; i++){
      if (isPrime(i)==0){
         fact1 = i; 
         for (j=0;j<n;j++){
            if (isPrime(j)==0){
               fact2=j; 
               if (n == fact1*fact2){
                  return 0;
               }
            }
         }
      }
   }
   return -1;
}  
