import java.io.*;
import java.util.Scanner;

public class Grading_Students {
    public static void main(String[] args) {
        int grade, no_students;
        Scanner Sc = new Scanner(System.in);
        no_students = Sc.nextInt();
        int[] gradeArray = new int[no_students];
        int temp = no_students;
        for (int i=0; i< no_students; i++) {
            gradeArray[i] = Sc.nextInt();
        }
        for(int i=0; i< no_students; i++) {
            int te = (gradeArray[i] / 5 + 1);
            if (gradeArray[i] < 38) {
                ;
            } else if ((te*5) - gradeArray[i] < 3) {
                gradeArray[i] += (te*5) - gradeArray[i];
            }
        }

        for(int i=0; i< gradeArray.length; i++) {
            System.out.println(gradeArray[i]);
        }
    }
}