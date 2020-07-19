#include <stdio.h>
#include "ll.h"

int main(void) {
   llnode *root = NULL;
   llnode *root2 = NULL; 
   int r=0;
   int i=0;
   int test = 10; 
   int del_val = 400;
   int insert = 0; 

   printf("List A\n");
   r=ll_add_to_tail(&root,100);
   r=ll_add_to_tail(&root,200);
   r=ll_add_to_tail(&root,300);
   for(i=0;i<10;i=i+1){
      r=ll_add_to_tail(&root,i*100);
   }
   r=ll_print(root);
      
   /*Testing function ll_find_by_value*/
   test = ll_find_by_value(root,100);
   printf("Result for search for 100 is %d \n", test);
   test = ll_find_by_value(root,300);
   printf("Result for search for 300 is %d \n", test);
   test = ll_find_by_value(root,150);
   printf("Result for search for 150 is %d \n", test); 
  
   /*Testing ll_del_from_tail*/
   printf("\n");
   printf("Deleted from tail\n");
   r = ll_del_from_tail(&root);

   /*Testing ll_del from head*/
   printf("Deleted from head\n");
   r = ll_del_from_head(&root);

   /*Testing ll_del with value*/
   printf("Deleted value %d\n", del_val);
   r = ll_del_by_value(&root, del_val);
   
   /*Testing ll_insert_in_order*/
   printf("Inserting %d to list\n", insert); 
   r = ll_insert_in_order(&root,insert);
   r = ll_print(root);
  
  /* Testing insert in order */
   printf("\nList B\n");
   root2=NULL;
   r=ll_add_to_tail(&root2,100);
   r=ll_add_to_tail(&root2,200);
   r=ll_add_to_tail(&root2,300);
   for(i=0;i<10;i=i+1){
      r=ll_add_to_head(&root2,i*100);
   }
   r=ll_print(root2);
     
   printf("\nList B concat to List A:\n");   
   r = ll_concat(&root, &root2);
   r = ll_print(root);
   
  printf("\nSorted List B\n");
   r = ll_sort(&root2);
   r = ll_print(root2);
   printf("\nSorted List A\n");
   r = ll_sort(&root); 
   r = ll_print(root);
   r = ll_free(root);
   r = ll_free(root2);
   return 0;
}
