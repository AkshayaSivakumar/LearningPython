# -problem3_6.py *- coding: utf-8 -*-

import sys

infile = sys.argv[1]
outfile = sys.argv[2]
    
inputfile = open(infile)    
outputfile = open(outfile, 'w')
   
for line in inputfile:
    charct = len(line.strip("\n"))
    outputfile.write(str(charct)+"\n")

inputfile.close() 
outputfile.close()
