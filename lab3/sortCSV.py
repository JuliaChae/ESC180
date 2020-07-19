# It is best to name your arguments rather than relying on position;
# this enables a user to use your program without memorizing
# argument order. This is a standard industrial practice.
# Below, you see that there are two named arguments that each take
# an additional parameter:
# --fin <ADDITIONAL-PARAM> --fout <ADDITIONAL-PARAM>
# This may be used in a program that takes in the name of
# an input and output file, in order to do further processing.
# You may modify this template for your purposes.
#
# The loop that is iterating over all the input arguments begins at
# 1, since sys.argv[0] is always the name of the program
# (in this case, "argtest.py", unless you renamed it).
# The loop is incrementing one arg at a time; since --fin and --fout
# take an additional argument, I created a variable called "skip"
# that enables you to skip over the filename during the looping
# since the --fin and --fout processing will always look at and
# consume the next argument. Note that I test to ensure
# --fin or --fout always have a trailing argument. Otherways, the
# program will give an "out of range" warning.
#
# This is course content. You must understand this. To understand this
# use it, modify it and experiment with it.
#
# usage: python argtest.py --fin blah_in --fout blah_out
# where you may change the names blah_in and blah_out as needed
#
# mathaine@ecf.utoronto.ca


import sys

FIN=""
FOUT=""
COL = ""
DIR = ""
nargs=len(sys.argv)
skip=False
for i in range(1,nargs):
   if not skip:
      arg=sys.argv[i]
      print("INFO: processing",arg)
      if arg == "--fin":
         if i != nargs-1:
            FIN=sys.argv[i+1]
            skip=True
      elif arg == "--fout":
         if i != nargs-1:
            FOUT=sys.argv[i+1]
            skip=True
      elif arg == "--col":
         if i != nargs -1:
            try:
               COL = int(sys.argv[i+1])
            except:
               print("ERR: Please enter an integer column value")
            skip = True
      elif arg == "--dir":
         if i!= nargs -1:
            DIR = sys.argv[i+1]
            skip = True
      else:
         print("ERR: unknown arg:",arg)
   else:
      skip=False

f = open(FIN,'r')
lines = f.readlines()
f.close()
accum=[]
for i in lines:
   j = i.split('\n')[0]
   k = j.split(',')
   r = []
   for x in k:
      r = r+ [float(x)]
   if COL>= len(r):
      print("ERR: Please enter a valid column value")
      break
   else:
      accum = accum + [r]
#print (accum)

def genSortKey(col,up):
   def key(x):
      return x[col] if up else -x[col]
   return key

if DIR == "+":
   sortKey = genSortKey(COL,True)
elif DIR == "-":
   sortKey = genSortKey(COL,False)

sortedaccum = sorted(accum,key=sortKey)

g=open(FOUT,'w')
for line in sortedaccum:
   for elindex in range(0,len(line)):
      if elindex!=len(line)-1:
         g.write(str(line[elindex])+",")
      else:
         g.write(str(line[elindex])+"\n")
g.close()

print("INFO: FIN",FIN)
print("INFO: FOUT",FOUT)
print("INFO: COL", COL)
print("INFO: DIR", DIR)
