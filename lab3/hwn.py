"""This program takes in an integer (n) and string (msg)  input to print the string is printed "n" times"""

def hwn(msg, n):
   for x in range (0,n):
      print(msg)
   return True

def main():
   valn = int(input())
   valmsg = input()
   hwn (valmsg, valn)
   return True 

main()
