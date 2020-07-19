#include<stdio.h>

int bubblesort(int *array, int size);

int main(void){
   int i;
   int m[10]={3,2,5,33,6,4,2,7,8,12};
   for (i = 0; i<10; i++){
      printf("%d ",m[i]);
   }
   printf("\n");
   bubblesort(m, 10);
   for (i=0; i<10; i++){
      printf("%d ",m[i]);
   }
}

int bubblesort(int *array, int size){
   int n = size;
   int swapped = 1;
   int i; 
   int temp;
   if (array == NULL){
      return -1;
   }
   while (swapped == 1){
      swapped = 0;
      for (i=1; i<n; i++){
         if (array[i-1]>array[i]){
            temp = array[i-1];
            array[i-1] = array[i];
            array[i]=temp;
            swapped = 1;
         }
      }
   }
   return 1;
}


