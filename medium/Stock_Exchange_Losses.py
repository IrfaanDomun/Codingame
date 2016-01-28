import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
list = []
res =[0,0]
n = int(raw_input())
inputs = raw_input().split()
for i in xrange(n):
    v = int(inputs[i])
    list.append(v)
    res[0] = max(res[0],res[1]-v)
    res[1] = max(res[1],v)
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print -res[0]
