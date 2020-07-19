int anlBoard(int *T, int sizeT){
   int i;
   int indexH = 0;
   int indexV = 0;
   int xWin =0;
   int oWin =0;
   int xCount =0;
   int oCount =0; 
   if (sizeT != 9){ /* Errortraps for a list of the incorrect length */
      return -1;
   }
   for (i=0; i<sizeT;i=i+1){
      printf("The array elem %d, is %d \n", i, T[i]);
   }
   for (i=1;i<4;i=i+1){
      if ((T[indexH] == T[indexH+1]) && (T[indexH] == T[indexH+2])){
         if (T[indexH] == 1){
            xWin= xWin + 1;
         }
         else if (T[indexH] == 2){
            oWin = oWin + 1;
         }
      }
      if ((T[indexV] == T[indexV+3]) && (T[indexV] == T[indexV+6])){
         if (T[indexV] == 1){
            xWin= xWin + 1;
         }
         else if (T[indexV] == 2){
            oWin = oWin + 1;
         }
      }
      indexH = indexH + 3;
      indexV = indexV + 1;
      }
   if ((T[0]==T[4] && T[0] == T[8]) || (T[2]==T[4] && T[2]==T[6])){
      if (T[4] == 1){
         xWin = xWin + 1; 
      }
      else if (T[4] == 2){
         oWin = oWin + 1; 
      }
   }
   printf("%d", xWin);
   printf("%d", oWin);
   if ((xWin == 0) && (oWin ==0)){
      for (i=0;i<9;i++){
         if ((T[i]!=1) && (T[i]!=2)){
            return 0;
         }
      }
      return 3;  
   }
   else {
      if (xWin == oWin){
         return -1;
      }
      else if (xWin >= 1){
         return 1;
      }
      else if (oWin >= 1){
         return 2;
      }
      else{
         return -1;
      }
   }
   return 0;
}
