#include<stdio.h>

int bubbleSort(int *array, int size){
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
   return 0;
}


