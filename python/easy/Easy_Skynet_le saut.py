import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(raw_input()) # the length of the road before the gap.
gap = int(raw_input()) # the length of the gap.
platform = int(raw_input()) # the length of the landing platform.
jumped = False

# game loop
while 1:
    speed = int(raw_input()) # the motorbike's speed.
    coord_x = int(raw_input()) # the position on the road of the motorbike.
    if not jumped :
        if speed < gap+1:
        # Write an action using print
        # To debug: print >> sys.stderr, "Debug messages..."
    
        # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
            print "SPEED"
            print >> sys.stderr , speed,gap
        elif speed > gap + 1 :
            print "SLOW"
            
        elif coord_x <road-speed:
            print "WAIT"
            print >> sys.stderr,coord_x,road,"cooooooooooooc"
            
        else:
            print "JUMP"
            jumped = True
    else:
        print "SLOW"
    
