#include<stdio.h>
#include"sort.c"
int bubbleSort(int *array, int size);

int main(void){
   int i;
   int m[10]={3,2,5,33,6,4,2,7,8,12};
   for (i = 0; i<10; i++){
      printf("%d ",m[i]);
   }
   printf("\n");
   bubbleSort(m, 10);
   for (i=0; i<10; i++){
      printf("%d ",m[i]);
   }
}


