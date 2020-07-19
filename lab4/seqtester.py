from seqdetectorlib import *

def main():
   x = seqdetector()
   n = 0
   while True:
      word = input("Enter a word :" ) 
      status = x.evolve(word)
      print(status)
      if status == True:
         print ("Detected")
         break 
   return True 

main()

