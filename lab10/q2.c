#include <stdio.h>

struct blah {
   int id;
   int val[4];
   char label[4];
   int *data; 
};

int main(void){
   printf("%d", sizeof(struct blah));
}

/*The answer is 32 bytes*/
