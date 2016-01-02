import sys
import math
import bisect
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

 # w: width of the building.
 # h: height of the building.
w, h = [int(i) for i in raw_input().split()]
n = int(raw_input()) # maximum number of turns before game over.
x0, y0 = [int(i) for i in raw_input().split()]
print >> sys.stderr,w,h
# game loop
x,y = x0,y0
x0 = 0
y0 = 0
while 1:
    bomb_dir = raw_input() # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    print >> sys.stderr,bomb_dir,x0,y0,w,h,x,y 
    # the location of the next window Batman should jump to.
    if 'D' in bomb_dir:
        y0 = y
        y = (y+h)//2
        
    if 'U' in bomb_dir:
        h = y
        y = y0 +(y-y0)//2
    if 'R' in bomb_dir : 
        x0 = x
        x = (x+w)//2
    if 'L' in bomb_dir : 
        w = x
        x = x0+ (x-x0)//2
    print str(x)+' '+str(y)
        
