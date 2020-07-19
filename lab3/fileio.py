def filereader():
   FIN = "datain"
   try: 
      f = open(FIN,'r')
   except:
      print("ERR: FILE", FIN, "is not present or can't be opened")

   lines = f.readlines()

   for line in lines:
      print(line.split('\n')[0])
   
   f.close()

def filewriter():
   FOUT = "dataout"
   try:
      g = open(FOUT,'w')
   except:
      print("ERR: FILE",FOUT, "is not present or can't be written to")

   g.write("This is content\n")
   g.write("This is more content\n")

   g.close()

def csvreader():
   FIN = "data"
   sortKey = genSortKey(2,False)
   try:
      f = open(FIN, 'r')
   except:
      print("ERR: FILE",FIN,"is not present or can't be opened")
   
   lines = f.readlines()
   f.close()
   accum = []
   for i in lines:
      j = i.split('\n')[0] # first get rid of the '\n' 
      k = j.split(',') # now split on the comma 
      r = []
      for x in k:
         r = r + [int(x)]
      accum = accum + [r] #accumulate 
   print(accum)
   print(sorted(accum))
   print(sorted(accum,key=sortKey))

"""
# returns key value that serves as the criterion to sort with
def sortKey(x):
   return x[2] # make negative, ir you want to sort in reverse order 
"""

def genSortKey(col,up):
   def key(x):
      return x[col] if up else -x[col]
   return key

csvreader()
