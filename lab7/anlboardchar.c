int anlBoard(char *T, int sizeT){
   int i;
   int intArray[9];
   int indexH = 0;
   int indexV = 0;
   int xWin =0;
   int oWin =0;
   int xCount =0;
   int oCount =0; 
   if (sizeT != 9){ /* Errortraps for a list of the incorrect length */
      return -1;
   }
   for (i=0; i<9; i = i+1){
      if (T[i]=='X'){
         intArray[i] = 1;
      }
      else if (T[i]=='O'){
         intArray[i]=2;
      }
      else if (T[i] == '-'){
         intArray[i]=0;
      }   
   }
   for (i=0; i<sizeT;i=i+1){
      printf("The array elem %d, is %c \n", i, T[i]);
   }
   for (i=1;i<4;i=i+1){
      if ((intArray[indexH] == intArray[indexH+1]) && (intArray[indexH] == intArray[indexH+2])){
         if (intArray[indexH] == 1){
            xWin= xWin + 1;
         }
         else if (intArray[indexH] == 2){
            oWin = oWin + 1;
         }
      }
      if ((intArray[indexV] == intArray[indexV+3]) && (intArray[indexV] == intArray[indexV+6])){
         if (intArray[indexV] == 1){
            xWin= xWin + 1;
         }
         else if (intArray[indexV] == 2){
            oWin = oWin + 1;
         }
      }
      indexH = indexH + 3;
      indexV = indexV + 1;
      }
   if ((intArray[0]==intArray[4] && intArray[0] == intArray[8]) || (intArray[2]==intArray[4] && intArray[2]==intArray[6])){
      if (intArray[4] == 1){
         xWin = xWin + 1; 
      }
      else if (intArray[4] == 2){
         oWin = oWin + 1; 
      }
   }
   printf("%d", xWin);
   printf("%d", oWin);
   if ((xWin == 0) && (oWin ==0)){
      for (i=0;i<9;i++){
         if ((intArray[i]!=1) && (intArray[i]!=2)){
            return 0;
         }
      }
   }
}
