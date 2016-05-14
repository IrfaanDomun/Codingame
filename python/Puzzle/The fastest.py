import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def str2sec(t):
    h = int(t[:2])*3600
    m = int(t[3:5])*60
    s = int(t[6:8])

    return h+m+s

dic = {}

n = int(raw_input())
for i in xrange(n):
    t = raw_input()
    key = str2sec(t)
    dic[key] = t

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print dic[min(dic.keys())]
