import time
t = time.time()
import sys
import math
import itertools
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


n = int(raw_input())
list_puissance = []
dic = {}
res = []
for i in xrange(n):
    pi = int(raw_input())
    list_puissance.append(pi)
#print 1
#print t-time.time(), len(list_puissance),len(set(list_puissance)),list_puissance[:10],list_puissance[-10:]
list_puissance.sort()
for i in range(len(list_puissance)):
    try:
        res.append(abs(list_puissance[i] - list_puissance[i+1]))
    except:
        pass
print min(res)
#for a,b in itertools.combinations(set(list_puissance),2):
#   dic[abs(a-b)]=[a,b]
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
#print min(dic.keys())
