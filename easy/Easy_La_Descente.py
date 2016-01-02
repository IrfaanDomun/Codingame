import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while 1:
    plus_haut =-1
    indice_haut = 1
    space_x, space_y = [int(i) for i in raw_input().split()]
    for i in xrange(8):
        mountain_h = int(raw_input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        if mountain_h > plus_haut:
            plus_haut = mountain_h
            indice_haut = i
    if space_x == indice_haut :
        print "FIRE"
    else :


    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).
        print "HOLD"
