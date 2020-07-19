# counterlib class testing code
from counterlib import *

def main():
   x= counter(1000)
   y= counter(50)
   z = counter(-90) 
   x.evolve(10)
   x.evolve(25)
   x.evolve(10)
   y.evolve(x.getState())
   z.evolve(15)
   print("Checking counter x: 1000 + 10 + 25 + 10 = "+str(x.getState()))
   print("Adding " + str(x.getState()) + " to 50 is " + str(y.getState()))
   print("Sum of three counters " + str(x.getState()) + ", " + str(y.getState()) + ", and "+str(z.getState())+" is " + str(x.getState() + y.getState() + z.getState()))

main()

