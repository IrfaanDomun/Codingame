import sys
import math

def median(lst):
    lst = sorted(lst)
    if len(lst) < 1:
            return None
    if len(lst) %2 == 1:
            return lst[((len(lst)+1)/2)-1]
    else:
            return int(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))//2 
            
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
list_x = []
list_y = []

n = int(raw_input())
for i in xrange(n):
    x, y = [int(j) for j in raw_input().split()]
    list_x.append(x)
    list_y.append(y)
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
x_max = max(list_x) 
x_min = min(list_x)

res_med = median(list_y)
res =  sum([ abs(j-res_med) for j in list_y])

print >> sys.stderr, res,res_med
print str( x_max - x_min  + res )
