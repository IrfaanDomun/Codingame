import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
"""""
Get the data
"""
l, c, n = [int(i) for i in raw_input().split()]
list_people = []
for i in xrange(n):
    pi = int(raw_input())
    list_people.append(pi)
print >> sys.stderr,list_people,l,c,n
"""""
Compute for each day the  number of people who ride it with the constraint
"""
res = 0
previous_sum = 0
for k in range(c):
    print >> sys.stderr,'...................'
    for i in range(len(list_people)):
        sum_temp = sum(list_people[:i])
        print >> sys.stderr, list_people, list_people[i:], list_people[:i],i,sum_temp,res,l
        
        if sum_temp > l:
            res = previous_sum

            list_people = list_people[i-1:] + list_people[:i-1]
            break
        else:
            previous_sum = sum_temp
    print >> sys.stderr, res

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print res
