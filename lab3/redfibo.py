"""returns the product of all fibo numbers specified"""

def reduce(func,elist):
   product=elist[0]
   for index in range(1,len(elist)):
      product = func(product, elist[index])
   return product 

def fibo(n):
   if n == 0 or n == 1:
      return 1
   else:
      return fibo(n-1) + fibo(n-2)

def fiboL(n):
   fiboList = []
   for x in range(0,n+1):
      fiboList = fiboList + [fibo(x)]
   return fiboList

def mult(a,b):
   return a*b
      
def redfibo(n):
   return reduce(mult, fiboL(n))
