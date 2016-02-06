import itertools

"""""
Guetting the data
"""
n = int(raw_input())
list_sequence = []
for i in xrange(n):
    subseq = raw_input()
    list_sequence.append(subseq)    
"""""
Guetting ride of duplicate
"""
list_sequence = list(set(list_sequence))
"""""
Remove all word which is already contained in another
"""
for a,b in itertools.permutations(list_sequence,2):
    if a in b :
        list_sequence.remove(a)
"""""
Try all the permutation of sequences and take the shortest
"""
res = []
list_index_permutation = itertools.permutations(range(len(list_sequence)))
for indexes_permutation in list_index_permutation:
    res_temp = list_sequence[indexes_permutation[0]]
    for index in range(len(indexes_permutation)):
        """""
        Go throught all permutation until we break out of the index
        """
        try:
            a = list_sequence[indexes_permutation[index]]
            b = list_sequence[indexes_permutation[index +1]]
            hold_temp = res_temp[:]
            """""
            Find the best way to merge the two sequences without losing information
            """
            for i in range(1,len(a)):                
                if b.startswith(a[i:]):                    
                    res_temp = res_temp + b[-(-len(a[i:])+len(b)):]
                    break
            """""
            If they are no commun ground add the new sequence
            """
            if hold_temp == res_temp:
                res_temp = res_temp + b 
        except:
            """""
            When we break out of the index append the length of the result
            """
            len_temp = len(res_temp)
            if len_temp not in res:
                res.append(len_temp)
"""""
print the min of the sequence's length
"""
print min(res)
