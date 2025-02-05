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
   if state == 1:
      printBoard(T)
      print ("X has won the game!")
      break
   elif state == 3:
      printBoard(T)
      print ("The game is a draw!")
      break 

   if genWinningMove(T, 2)!=-1:
      T[genWinningMove(T,2)] = 2
   elif genNonLoser(T,2)!= -1:
      T[genNonLoser(T,2)] = 2
   else:
      T[genRandomMove(T,2)] = 2
   state = analyzeBoard(T)
   if state == 2:
      printBoard(T)
      print("O has won the game!")
      break
   elif state == 3:
      printBoard(T)  
      print ("The game is a draw!")
      break
