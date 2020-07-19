#include <stdio.h>


int print2d_2x3(int p[2][3]){
   /* least generic: fixed for 2x3 arrays */
   int x,y;
   for(x=0;x<2;x=x+1){
      for(y=0;y<3;y=y+1){
         printf("%3d ",p[x][y]);
      }
      printf("\n");
   }
   return 0;
}


int main(void) {
   int arr2d[2][3];
   int x=0, y=0;
   int i=0;
   int r=0;

   i=0;
   for(x=0;x<2;x=x+1){
      for(y=0;y<3;y=y+1){
         arr2d[x][y]=i;
         i=i+1;
      }
   }
   printf("Method A\n");
   r=print2d_2x3(arr2d);
}

