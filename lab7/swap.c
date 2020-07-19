int swap(int *a, int *b){
   int temp=*b;
   *b = *a; 
   *a = temp;
   printf("a is %d", *a);
   printf("b is %d", *b);
   return 1;
   }
