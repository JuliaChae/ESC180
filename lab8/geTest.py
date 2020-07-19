from ge import *

def main():
   matrix = [[2.0,1.0,1.0,1.0],[1.0,1.0,3.0,4.0],[2.0,3.0,2.0,0.0]]
   print("Forward Matrix:" +str(gw_fw(matrix)))
   print("Backward Matrix:" +str(gw_bw(gw_fw(matrix))))
   #print(matrix)

main()
