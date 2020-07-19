#include <stdio.h>

int fibo(int n); 
/*
int main(void){
   printf("%d", fibo(5));
}*/

int fibo(int n){
   if (n==0 || n==1 || n==2){
      return 1;
   } else if (n<0) {
      return 0;
   }else {
      return fibo(n-1) + fibo (n-2) + fibo(n-3);
   } 
   
}


