"""This library defines a class for an object counter and includes functions to increment and return the value of the object."""

class counter: 
   def __init__(self, initCnt):
      self.cnt = initCnt 

   def evolve(self, x):
      self.cnt = self.cnt + x
      return True

   def getState(self):
      return self.cnt
