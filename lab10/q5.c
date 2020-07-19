#include <stdio.h>

int g(char **array, int n);

int g(char **array, int n){
  if (size <= 0){
     return -1;}
  if (array==NULL){
     return -1;}
  (*array) = (char *)malloc(n*sizeof(char));
  return 0;
}
