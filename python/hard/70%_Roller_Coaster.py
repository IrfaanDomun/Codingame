import sys
import math
"""""
Get the data
"""
l, c, n = [int(i) for i in raw_input().split()]
list_people = []
for i in xrange(n):
    pi = int(raw_input())
    list_people.append(pi)
"""""
Compute for each day the  number of people who ride it with the constraint
"""
res = 0
previous_sum = 0
sum_people = sum(list_people)
for k in range(c):    
    
    if sum_people < l:
        """ 
        If the total number of people in the list is not enough to fill the capacity
        """        
        res += sum_people
    else:
        """""
        If they are more people than the roller coaster's capacity
        """
        for i in range(len(list_people)+1):
            sum_temp = sum(list_people[:i])
            print >> sys.stderr, list_people, list_people[i:], list_people[:i],i,sum_temp,res,l
            
            if sum_temp > l:
                res += previous_sum
    
                list_people = list_people[i-1:] + list_people[:i-1]
                break
            else:
                previous_sum = sum_temp
print res
