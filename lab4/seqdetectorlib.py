"""This program contains a class whih creates a statemachine object which recognizes a specific sequence of words"""

class seqdetector: 
   
   def __init__(self):
      self.state = "NULL"
      self.seq = [] 
      self.sol = ["here", "are", "the", "solutions", "to", "the", "next", "exam"]

   def evolve(self, word):
      self.seq = self.seq + [word] 
      for i in range(0,len(self.seq)):
         if self.seq[i] != self.sol[i]:
            self.state = "NULL"
            self.seq = []  
            break
         elif i == len(self.sol)-1:
            self.state = "UNLOCKED"
         else:
            self.state = "DETECTING..."
      if self.state == "UNLOCKED":
         return True
      else:
         return False

            
      
         
      
 
