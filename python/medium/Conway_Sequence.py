import sys
import math
from itertools import groupby
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(raw_input())
l = int(raw_input())
res = [r]

for i in range(l-1):
    """
    goup by number of occurence and transform to a list
    """
    res = [( sum(1 for i in g),k) for k,g in groupby(res)]
    res = [j for i in res for j in i]

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
res = " ".join(map(str,res))
print res 
