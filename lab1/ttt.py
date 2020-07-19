"""This allows a user to play a 2 player tic tac toe game"""

from tttlib import *

T = genBoard()
while True:
   printBoard(T)
   while True:
      moveX = input("X move? ")
      print("")
      if (moveX =="0" or moveX =="1" or moveX =="2" or moveX =="3" or moveX =="4" or moveX =="5" or moveX =="6" or moveX =="7" or moveX =="8") and int(moveX)<9 and T[int(moveX)]==0:
         T[int(moveX)] = 1
         break
      else:
         print ("Please enter a valid input")
         print("")
   state = analyzeBoard(T)
   print(state)
   if state == 1:
      printBoard(T)
      print ("X has won the game!")
      break
   elif state == 3:
      printBoard(T)
      print ("The game is a draw!")
      break 

   print(T)
   printBoard(T)
   while(True):
      moveO = input("O move? ")
      print("")
      if (moveO =="0" or moveO =="1" or moveO =="2" or moveO =="3" or moveO =="4" or moveO =="5" or moveO =="6" or moveO =="7" or moveO =="8") and int(moveO)<9 and T[int(moveO)] ==0:
         T[int(moveO)]=2
         break 
      else:
         print ("Please enter a valid input")
         print("")
   state = analyzeBoard(T)
   print(state)
   if state == 2:
      printBoard(T)
      print("O has won the game!")
      break
   elif state == 3:
      printBoard(T)  
      print ("The game is a draw!")
      break
