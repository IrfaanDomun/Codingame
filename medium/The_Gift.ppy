import sys
import math
""""
Get the data
"""
n = int(raw_input())
c = int(raw_input())
list_budget = []
for i in xrange(n):
    b = int(raw_input())
    list_budget.append(b)
    print >> sys.stderr,list_budget
"""""
If the gift can be paid
"""
if sum(list_budget) >= c:
    fair_share = c/n
    paid_so_far = 0
    """"
    Checking from the poorest the richest Ood 
    if they can pay the fair shade and report it otherwise on the richer
    """
    list_budget = sorted(list_budget)    
    for i in range(len(list_budget)):
        budget_temp = list_budget[i]
        fair_share = (c - paid_so_far)/(n-i)
        """""
        If he can't pay the fair share, he pay all he have else he pays it
        """
        if budget_temp < fair_share :
            print budget_temp 
            paid_so_far += budget_temp            
        else :
            print fair_share
            paid_so_far += fair_share 
else : 
    """"
    If the gift can't be paid
    """
    print "IMPOSSIBLE"
