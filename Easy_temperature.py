import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input()) # the number of temperatures to analyse
temps = raw_input() # the n temperatures expressed as integers ranging from -273 to 5526
if temps == "":
    print "0"
else :
    temp_list = temps.split()
    print >> sys.stderr, temps,type(temp_list[0])
    temp_list = map(int,temp_list)
    temp_list_abs = map(abs,temp_list)
    temp_temps =min(temp_list_abs)
    if temp_temps in temp_list:
        print temp_temps
    else : 
        print "-"+str(temp_temps)
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

#print "result"
