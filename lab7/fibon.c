#include <stdio.h>

int fibo(int n);

int main(void) {
   int i;
   int n;
   printf("Enter how many fibonacci numberes you want: ");
   scanf("%d", &n);
   for (i=0;i<n;i=i+1){
      int f= fibo(i);
      printf("fibo(%d)=%d\n",i,f);
   }
   return 0;
}

int fibo(int n){
   int base = 1;
   if (n ==0){
      return base;
   }
   else if (n==1){
      return base;
   }
   else {
      return fibo(n-1) + fibo(n-2);
   }
}
