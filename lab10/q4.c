#include <stdio.h>

int f(int x);

int main(void)
{
   printf("%d",f(5));
}

int f(int x){
   if (x==-1){
      return 2;
   } else {
      return x*f(x-2);
   }
}

/* It is 30 */
