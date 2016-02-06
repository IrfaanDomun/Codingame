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

        // game loop
        while (true) {
            /**
             * Get the data
            */
            int spaceX = in.nextInt();
            int spaceY = in.nextInt();
            int [] listMountain = new int[8];
            for (int i = 0; i < 8; i++) {
                int mountainH = in.nextInt(); // represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
                listMountain[i] = mountainH;
            }
            /**
             * find the moutains to shoot
             */
             int indexToShoot = -1; 
             int maxHeight = -1;
             for (int i =0; i < 8;i++){
                 if(maxHeight < listMountain[i]){
                  indexToShoot = i;
                  maxHeight = listMountain[i];
                 }
             }
            /**
             * Decide chether of not to shoot
             */
             if(spaceX == indexToShoot){
                 System.out.println("Fire");
             }
             else{
                 System.out.println("Hold");
             }
 }
    }
}
