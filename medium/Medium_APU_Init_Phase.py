import sys
import math
# Don't let the machines win. You are humanity's last hope...

width = int(raw_input()) # the number of cells on the X axis
height = int(raw_input()) # the number of cells on the Y axis
print >> sys.stderr, width, height
line = []
for i in xrange(height):
    line.append(raw_input()) # width characters, each either 0 or .
    print >> sys.stderr, line
for i in range(len(line)):
    for j in range(len(line[i])):
        

        res = ''
        if line[i][j] == '0':
            res = str(j) + ' ' +str(i)+ ' '
            ligne = j
            colone = i
            while True:
                try : 
                    if line[colone][ligne+1] == '0': 
                        res = res + str(ligne+1) + ' '+str(colone)+' '
                        break
                    else : 
                        pass
                    ligne = ligne +1
                except:
                    res = res + '-1 -1 '
                    break
                
            ligne = j 
            while True:
                try : 
                    if line[colone+1][ligne] == '0': 
                        res = res + str(ligne) + ' '+str(colone+1)+' '
                        break
                    else : 
                        pass
                    colone = colone +1
                except:
                    res = res + '-1 -1 '
                    break                
            print >> sys.stderr,line[i][j],"kn;,n",res
            print res
                
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

# Three coordinates: a node, its right neighbor, its bottom neighbor
print "0 0 1 0 0 1"
