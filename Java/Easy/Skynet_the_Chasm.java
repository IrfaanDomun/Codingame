import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int road = in.nextInt(); // the length of the road before the gap.
        int gap = in.nextInt(); // the length of the gap.
        int platform = in.nextInt(); // the length of the landing platform.
        boolean jumped = false;
        // game loop
        while (true) {
            int speed = in.nextInt(); // the motorbike's speed.
            int coordX = in.nextInt(); // the position on the road of the motorbike.
            /**
             * If we didn't jumped yet
             */
            if( jumped == false){
                if(speed < gap + 1){
                    System.out.println("SPEED");   
                }
                else if( speed > gap +1){
                    System.out.println("SLOW");   
                }
                else if(coordX < road - speed){
                    System.out.println("WAIT");
                }
                else{
                    System.out.println("JUMP");
                    jumped = true;
                }
            }
            /**
             * If we did, slow down
             */
            else {
                System.out.println("SLOW");
            }

        }
    }
}
