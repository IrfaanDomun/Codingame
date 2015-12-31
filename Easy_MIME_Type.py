import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input()) # Number of elements which make up the association table.
q = int(raw_input()) # Number Q of file names to be analyzed.
dict = {}
lis = []
list_ = []

for i in xrange(n):
     # ext: file extension
     # mt: MIME type.
    ext, mt = raw_input().split()
    dict[ext.lower()] = mt
print >> sys.stderr,dict
for i in xrange(q):
    fname = raw_input() # One file name per line.
    if '.' in fname:
        lis.append(fname.split(".")[-1])
    else :
        lis.append("chips")
    list_.append(fname)
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
print >> sys.stderr,lis
print >> sys.stderr,list_

for i in lis:
    try :
        print dict[i.lower()]
    except : 
        print 'UNKNOWN'
        
# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
