# -*- coding: utf-8 -*-
#%%
"""
Created on Sat May 15 20:08:43 2021

@author: Akshaya V S
"""
import sys

infilename = sys.argv[1]
outfilename = sys.argv[2]

infile = open(infilename)
outfile = open(outfilename,'w')
    
for line in infile:
    outfile.write(line)
        
infile.close()
outfile.close()

