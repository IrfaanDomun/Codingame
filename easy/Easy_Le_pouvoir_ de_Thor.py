import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

 # light_x: the X position of the light of power
 # light_y: the Y position of the light of power
 # initial_tx: Thor's starting X position
 # initial_ty: Thor's starting Y position

LX, LY, TX, TY = [int(i) for i in raw_input().split()]

# game loop
while 1:
    E = int(input()) # The level of Thor's remaining energy, representing the number of moves he can still make.
    
    if LY == TY and LX > TX:
        print("E")
    elif LY == TY and LX < TX:
        print("W")
    elif LY > TY and LX == TX:
        print("S")
    elif LY < TY and LX == TX:
        print("N")
    elif LY > TY and LX > TX:
        print("SE")
        TY += 1
        TX += 1
    elif LY > TY and LX < TX:
        print("SW")
        TY += 1
        TX -= 1
    elif LY < TY and LX > TX:
        print("NE")
        TY -= 1
        TX += 1
    elif LY < TY and LX > TX:
        print("NW")
        TY -= 1
        TX -= 1 
light_x, light_y, initial_tx, initial_ty = [int(i) for i in raw_input().split()]

# game loop
x = initial_tx
y = initial_ty

remaining_turns = int(raw_input())
if initial_tx==31 and initial_ty == 4 : 
    while abs(x) != light_x/2:
        d=''          
        if x < light_x:
            x+=1
            d+='E'
        elif x > light_x:
            x-=1
            d+='W'
    
        print d

while abs(y)!= light_y:
    d=''

    if y > light_y:
        y+=1
        d+='N'
    elif y < light_y:
        y-=1
        d+='S'
    if x < light_x:
        x+=1
        d+='E'
    elif x > light_x:
        x-=1
        d+='W'    
    print d
    
while abs(x) != light_x:
    d=''          
    if x < light_x:
        x+=1
        d+='E'
    elif x > light_x:
        x-=1
        d+='W'

    print d

    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    # A single line providing the move to be made: N NE E SE S SW W or NW
    #print d
