import sys
import math
from collections import defaultdict
import time
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
t = time.time()
"""""
Get the data into a dictionary of day for keys and a list of durations of calculation
"""
n = int(raw_input())
dico = defaultdict( lambda :[])
for i in xrange(n):
    j, d = [int(j) for j in raw_input().split()]
    dico[j].append( d)

print >> sys.stderr, '.................................',len(dico.keys()),sorted(dico.keys())
"""""
start with the first day as we use a greedy approach
"""
res = 0
list_day = sorted(dico.keys())
i = 0
current_day = list_day[i]
current_shortest_duration = sorted(dico[current_day])[0]
i = i + 1 
res = res + 1 
"""""
Look for the next day with our starting point which the computation can be made
"""
while True :
    try:
        next_day = list_day[i]
        if current_shortest_duration + current_day <= next_day :
            addition = 0
            sum_temp = 0
            sorted_current_day_computation = sorted(dico[current_day])
            for j in sorted_current_day_computation:
                sum_temp = sum_temp + j
                # print >> sys.stderr, 'i ',i,'sum ',sum_temp,' curent day ',current_day,' next ',next_day,'list',sorted(dico[current_day])
                if sum_temp + current_day <= next_day:
                    addition = addition + 1
                else : 
                    break
            res = res + addition
            current_day = next_day
            current_shortest_duration = sorted_current_day_computation[addition-1]
        i = i +1
    except IndexError:
        break
print >> sys.stderr,time.time()-t
# print 7879
print res 
