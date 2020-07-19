from conwaylib import *

def main():
   con = conway(10,12,"zeros")
   print(con.setPos(0,0,1))
   con.getmainList()
   con.printDisp()
   print(con.getNeighbours(0,0))
   print(con.getNeighbours(1,0))

main()
