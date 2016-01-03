import sys
import math
import string
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
l = int(raw_input())
h = int(raw_input())
t = raw_input()

def create_list_res(h,list_n):
    list_res = []
    for i in range(h):
        res = ''
        for n in list_n:
            res = res+list_alpha[i][n*l:(n+1)*l]
            
        list_res.append(res)
    return list_res

def create_list_n(t):
    list_n = []
    for i in t:
        try : 
            n = int(string.uppercase.index(i))
        except:
            try:
                n = int(string.lowercase.index(i))
            except:
                n=26
        list_n.append(n)
    return list_n
    
def create_list_alpha(h):
    list_alpha = []
    for i in xrange(h):
        row = raw_input()
        list_alpha.append(row) 
    return list_alpha
    
#create list of alphabet layes
list_alpha =create_list_alpha(h)
#create list of the letter's position in the alphabet from the inpu
list_n = create_list_n(t)
#create for each layer the according
list_res = create_list_res(h,list_n)
#print the layers
for i in list_res:
    print i
