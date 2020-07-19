"""This program generates a TicTacToe game where one player can play against another"""

import random

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

# Function that lets you place your move to prevent the opposition's win
def genNonLoser(T, player):
   for x in range(0,len(T)):
      Tcopy = list(T)
      if Tcopy[x] == 0:
         if player == 1:
            Tcopy[x]=2
            if analyzeBoard(Tcopy) == 2:
               return x
         elif player== 2:          
            Tcopy[x]=1
            if analyzeBoard(Tcopy) == 1:
               return x
         else:
            return -1
   return -1

# Function to determine the winning move 
def genWinningMove(T, player):
   for x in range(0,len(T)):
      Tcopy = list(T)
      if Tcopy[x] == 0:
         Tcopy[x] = player 
         if analyzeBoard(Tcopy) == player:
            return x
   return -1
 
# Randomly returns a potential move
def genRandomMove(T, player):
   if analyzeBoard(T) == 3:
      return -1
   randnum = random.randint(0,8)
   while T[randnum] != 0:
      randnum = random.randint(0,8)
   return randnum

# Returns the index of the first open space
def genOpenMove(T, player):
   for x in range(0,len(T)):
      if T[x] == 0:
         return x
      else:
         return -1

# test
#print(genOpenMove([1,2,1,1,2,1,2,1,2],2)) 
