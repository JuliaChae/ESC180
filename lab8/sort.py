def bubbleSort(array):
   n = len(array)
   swapped = True
   temp = 0
   while (swapped == True):
      swapped = False
      for i in range(1,n-1,1):
         if array[i-1]>array[i]:
            temp = array[i-1]
            array[i-1]=array[i]
            array[i]= temp
            swapped = True
   status = True
   return [status, array]


