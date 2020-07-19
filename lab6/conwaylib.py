import random 

class conway: 

   def __init__(self, listn, numelem, num):
      self.mainList = []
      self.inlist = []
      self.mainLength = listn
      self.subLength = numelem
      for i in range(0,listn,1):
         for x in range(0,numelem,1):
            if num == "zeros":
               self.inlist = self.inlist + [0]
            elif num == "ones":
               self.inlist = self.inlist + [1]
            elif num == "random":
               self.inlist = self.inlist + [random.randint(0,1)]
         self.mainList = self.mainList + [self.inlist] 
         self.inlist = []   

   def getmainList(self):
      return self.mainList

   def getDisp(self):
      returnString = ""
      for i in range(0, self.mainLength,1):
         element = self.mainList[i]
         for x in range(0,self.subLength,1):
            if element[x] == 0:
               returnString = returnString + " "
            elif element[x] == 1:
               returnString = returnString + "*"
            else:
               returnString = returnString + "ERR"
         returnString = returnString + "\n"
      return returnString

   def printDisp(self):
      print(self.getDisp())
      return True

   def setPos(self,row,col,val):
      if val == 1 or val ==0:
         self.mainList [row][col] = val
         return True 
      else:
         return False

   def getNeighbours(self, row, col):
      neighbourPos = [] 
      extendedWorld = [self.mainList[len(self.mainList)-1]] + list(self.mainList)+[self.mainList[0]]
      for i in range(0,len(extendedWorld),1):
         extendedWorld[i] = [extendedWorld[i][len(extendedWorld[i])-1]]+ extendedWorld[i] + [extendedWorld[i][0]]
      for i in range(row, row+3,1):
         for x in range(col, col+3,1):
            neighbourPos = neighbourPos + [extendedWorld[i][x]]
      neighbourPos = neighbourPos[0:4] + neighbourPos[5:]
      return neighbourPos 

   def evolve(self,rule):
      self.nextState = []
      inlist = []
      for i in range (0, self.mainLength, 1):
         for x in range(0,self.subLength, 1):
            inlist = inlist + [0]
         self.nextState = self.nextState + [inlist]
         inlist = []
      for i in range(0,self.mainLength,1):
         for x in range(0,self.subLength, 1):
            self.nextState[i][x] = rule(self.mainList[i][x], self.getNeighbours(i,x))
      self.mainList = list(self.nextState) 
      return True 
