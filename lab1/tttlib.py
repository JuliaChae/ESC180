"""This program generates a TicTacToe game where one player can play against another"""

# Returns a list corresponding to an unoccupied board
def genBoard():
   return [0,0,0,0,0,0,0,0,0]

# Checks the list for invalid inputs. Returns True if the list can be printed and is a valild TTT board. Returns False if there are any errors. Also Prints the TTT board
def printBoard(T):
   TPrint = []
   index = 0
   # Errortraps for an invalid input which is not a list
   if not (type(T) == list):
      return False
   # Errortraps for a list which doesn't have a length of 9 
   elif not(len(T) == 9):
      return False
   # Converts each element of the T list to their respective printable outputs and stores them in a list called printT 
   for x in T:
      if x == 0 or x == 1 or x ==2:
         if x == 0:
            TPrint = TPrint + [str(index)]
         elif x == 1:
            TPrint = TPrint + ["X"]
         elif x == 2:
            TPrint = TPrint + ["O"]
      else: 
         return False
      index= index + 1
   for x in range(0,7,3):
      print(" " + TPrint[x] + " | " + TPrint[x+1] + " | " + TPrint[x+2])
      print("---|---|---")
   return True

# Returns the state of the game
def analyzeBoard(T):
   indexH = 0
   indexV =0
   xWin = 0
   oWin = 0 
   xCount = 0
   oCount = 0
   # Errortraps for inconsistent number of Xs and Os
   for x in T:
      if x == 1:
         xCount = xCount + 1
      elif x == 2:
         oCount = oCount + 1
   if (oCount - xCount) > 1 or (xCount - oCount) > 1:
      return -1
   # Errortraps for an invalid input which is not a list
   if not (type(T) == list):
      return False
   # Errortraps for a list which doesn't have a length of 9 
   elif not(len(T) == 9):
      return False
   # Checking for wins 
   for x in range(1,4): 
      # Checking rows
      if (T[indexH]== T[indexH+1] and T[indexH] == T[indexH + 2]):
         if T[indexH] == 1:
            xWin = xWin + 1
         elif T[indexH] == 2:
            oWin = oWin + 1
      # Checking columns
      if (T[indexV]== T[indexV+3] and T[indexV] == T[indexV + 6]):
         if T[indexV] == 1:
            xWin = xWin + 1
         elif T[indexV] == 2:
            oWin = oWin + 1
      indexH = indexH + 3
      indexV = indexV + 1 
   # Checking for diagonal wins 
   if (T[0]==T[4] and T[0]==T[8]) or (T[2] == T[4] and T[2] == T[6]):  
      if T[4] == 1:
         xWin = xWin + 1
      elif T[4] == 2:
         oWin = oWin + 1
   # Checking if the game is over
   if xWin == 0 and oWin == 0:
      for x in T:
         # Game is still in play 
         if not (x == 1) and not (x == 2):
            return 0
      # Game is a draw
      return 3
   else:
      if xWin == oWin:
         return -1
      elif xWin >= 1:
         return 1
      elif oWin>= 1:
         return 2
      else:
         return -1

# test
"""print(printBoard([1,0,2,0,1,0,0,2,1]))
print(analyzeBoard([1,0,2,0,1,0,0,2,1]))
print(printBoard([2,0,0,1,1,1,0,2,0]))
print(analyzeBoard([2,0,0,1,1,1,0,2,0]))
print(printBoard([0,0,1,1,1,0,2,2,2]))
print(analyzeBoard([0,0,1,1,1,0,2,2,2]))
print(printBoard([1,0,2,0,2,1,2,1,0]))
print(analyzeBoard([1,0,2,0,2,1,2,1,0]))
print(printBoard([0,0,0,0,0,0,0,0,0]))
print(analyzeBoard([0,0,0,0,0,0,0,0,0]))
print(printBoard([1,2,1,2,1,1,2,2,1]))
print(analyzeBoard([1,2,1,2,1,1,2,2,1]))
print(printBoard([1,1,1,1,1,1,1,1,1]))
print(analyzeBoard([1,1,1,1,1,1,1,1,1]))
print(printBoard([1,2,1,2,1,1,1,2,1]))
print(analyzeBoard([1,2,1,2,1,1,1,2,1]))
"""

