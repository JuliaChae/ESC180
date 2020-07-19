def main():
   matrix = [[0.0,2.0,2.0,8.0],[1.0,3.0,3.0,9.0],[2.0,4.0,2.0,10.0]]
   print("Forward Matrix:" +str(gw_fw(matrix)))
   print("Backward Matrix:" +str(gw_bw(gw_fw(matrix))))
   #print(matrix)


def gw_fw(matrix):
   forwardM = [] 
   matrixM = list(matrix)
   counter = 0;
   for y in range(0,len(matrixM)):
      if matrixM[0][0] == 0:
         for i in range(0,len(matrixM)):
            if matrixM[i][0] != 0:
               orderedM = [matrixM[i]] + matrixM[0:i] + matrixM[i+1:]
               break; 
         #print(orderedM)
      else:
         orderedM = list(matrixM)
      for i in range(1,len(orderedM)):
         if orderedM[i][0] !=0:
            factor = orderedM[i][0]/orderedM[0][0]
            for x in range(0,len(orderedM[0])):
               orderedM[i][x] = orderedM[i][x]- (factor*orderedM[0][x])
         #print(orderedM)
      reducedMatrix = orderedM[1:]
      for i in range(0,len(reducedMatrix)):
         reducedMatrix[i] = reducedMatrix[i][1:]
      for i in range(0,counter):
         orderedM[0] = [0] + orderedM[0]
      forwardM = forwardM + [orderedM[0]]
      matrixM = list(reducedMatrix)
      counter = counter+1
   return forwardM

def gw_bw(matrix): 
   nonzero = 0;
   nonzeroIndex = 0;
   matrixM = list(matrix)
   factor =0 
   reducedM= []
   backwardM = list(matrix)
   for z in range(0,len(matrixM)):
      for x in range(0,len(matrixM[-1])):
         if matrixM[-1][x] !=0:
            nonzero = matrixM[-1][x]
            nonzeroIndex = x;
            break;
      for i in range(0,len(matrixM[0])):
         matrixM[-1][i] = matrixM[-1][i]/nonzero
      for i in range(0,len(matrixM)-1):
         factor = matrixM[i][nonzeroIndex]/matrixM[-1][nonzeroIndex]
         for x in range(0,len(matrixM[0])):
            #print(matrixM)
            matrixM[i][x] = matrixM[i][x] - factor*matrixM[-1][x]
         #print(matrixM[i])
      reducedM = matrixM[:-1]
      for i in range(0,len(reducedM)):
         backwardM[i] = reducedM[i]
      matrixM = list(reducedM)
   return backwardM
      
main()
