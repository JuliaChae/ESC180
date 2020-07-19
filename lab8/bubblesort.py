def main():
   l= [10,2,4,5,2,3,6,90]
   print(l)
   print(bubblesort(l))

def bubblesort(array):
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

main()
