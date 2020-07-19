def rule(value,listy):
   sum = 0
   for x in range(0,len(listy),1):
      sum = sum + listy[x]
   if value == 1:
      if sum == 2 or sum == 3:
         return 1
      else:
         return 0
   else:
      if sum == 3:
         return 1
      else:
         return 0
