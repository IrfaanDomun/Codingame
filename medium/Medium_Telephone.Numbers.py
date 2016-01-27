import sys
import math
from itertools import groupby
import os
import copy
import itertools
import bisect
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.            
liste = []
count = 0
n = int(raw_input())
for i in xrange(n):
    telephone = raw_input()
    bisect.insort_left(liste,telephone)
i=0
while True:
    if i != 0:
        past = liste[i-1]
    else :
        past = []
    try : 
        current = liste[i]
    except : 
        break
    temp_past = os.path.commonprefix( [current, past])    
    count +=   len(current) - len(temp_past)
    i = i+1
    
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

# The number of elements (referencing a number) stored in the structure.
print count
