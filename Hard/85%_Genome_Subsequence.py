import sys,os
import math
import itertools
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())
list_sequence = []
for i in xrange(n):
    subseq = raw_input()
    print >> sys.stderr, subseq
    list_sequence.append(subseq)
"""""
Remove all word which is conteined in another
"""
for a,b in itertools.permutations(list_sequence,2):
    if a in b :
        list_sequence.remove(a)

"""""
While they are still at least two word to permute
"""
longest_prefix = 1

while longest_prefix !=-1:
    """""
    Finding the longest commun prefix between two word
    """
    longest_prefix = -1
    first_string = ''
    second_string = ''
    print >> sys.stderr,'begin..............................',list_sequence
    

    for a,b in itertools.permutations(list_sequence,2):

        """""
        find longest prefix or sufix
        """
        a_prefix = -5
        a_sufix = -5
        for i in range(1,len(a)):
            print >> sys.stderr, a,b,i,a[:-i],b.endswith(a[:-i]),len(a[:-i])
            
            if b.endswith(a[:-i]):
                a_prefix = len(a[:-i])
                break
        for i in range(1,len(a)):
            print >> sys.stderr, a,b,i,a[i:],b.startswith(a[i:]),len(a[i:])

            if b.startswith(a[i:]):
                
                a_sufix = len(a[i:])
                break
                
        # print >> sys.stderr,a_prefix,b_prefix,a,b
                
        if a_prefix > longest_prefix or a_sufix > longest_prefix:
            if a_prefix > a_sufix:
                first_string = b
                second_string = a
                longest_prefix = a_prefix
            else :
                first_string = a
                second_string = b
                longest_prefix = a_sufix
                   
    """""
    Remove the two subseq from the list and add the new longest 
    """
    # print >> sys.stderr, first_string,second_string,longest_prefix,first_string[:-longest_prefix]+second_string,"................."
    print >> sys.stderr,list_sequence
    try : 
        list_sequence.remove(first_string)
        list_sequence.remove(second_string)
        if longest_prefix !=0:
            list_sequence.append(first_string[:-longest_prefix]+second_string)
        else :
            list_sequence.append(first_string+second_string)        
    except:
        pass

    
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
"""""
Print the len of the only element left which is the longest combinaison of subsequence without repetition
"""
print len("".join(list_sequence))
print>>sys.stderr,list_sequence
