import sys
import math
from collections import defaultdict
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

 # nb_floors: number of floors
 # width: width of the area
 # nb_rounds: maximum number of rounds
 # exit_floor: floor on which the exit is found
 # exit_pos: position of the exit on its floor
 # nb_total_clones: number of generated clones
 # nb_additional_elevators: ignore (always zero)
 # nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in raw_input().split()]
print >> sys.stderr,nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators
print >> sys.stderr,"nb_floors, width, nb_rounds, exit_floor, "
print >> sys.stderr,"exit_pos, nb_total_clones,"
print >> sys.stderr,"nb_additional_elevators, nb_elevators"
dic = {}
dic[exit_floor]=exit_pos
list_floor_blocked = [0 for i in range(nb_floors+1)]
for i in xrange(nb_elevators):
     # elevator_floor: floor on which this elevator is found
     # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in raw_input().split()]
    dic[elevator_floor]= elevator_pos
print >> sys.stderr,dic.items()
# game loop
while 1:
     # clone_floor: floor of the leading clone
     # clone_pos: position of the leading clone on its floor
     # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = raw_input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    print >> sys.stderr, clone_floor, clone_pos, direction
    print >> sys.stderr, "clone_floor, clone_pos, direction"
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    # action: WAIT or BLOCK
    if clone_floor != -1 : 
            if direction == 'LEFT':
                if clone_pos >= dic[clone_floor]:
                        print 'WAIT'
                else :
                    if list_floor_blocked[clone_floor]:
                        print 'WAIT'
                    else :
                        print 'BLOCK'
                        list_floor_blocked[clone_floor] = 1
            if direction == 'RIGHT':
                if clone_pos <= dic[clone_floor]:
                        print 'WAIT'
                else :
                    if list_floor_blocked[clone_floor]:
                        print 'WAIT'
                    else :
                        print 'BLOCK'
                        list_floor_blocked[clone_floor] = 1            
    else : 
        print 'WAIT'
        
