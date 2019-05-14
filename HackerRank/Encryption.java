
/**
 * 
 * https://www.hackerrank.com/challenges/encryption/problem
 */

import java.io.*;
import java.util.Scanner;
import java.lang.*;

public class Encryption {
    public static void main(String[] args) {

        Scanner Sc = new Scanner(System.in);
        String sentence;

        sentence = Sc.nextLine();
        sentence = sentence.replaceAll("\\s+", "");

        int len = sentence.length();
        int row = (int) Math.floor(Math.sqrt(len));
        int col = (int) Math.ceil(Math.sqrt(len));
        if ((row * col) < len) {
           row++;

        }

        char mat[][] = new char[row][col];

        int i = 0;
        while (i < len) {
            for (int j = 0; j < row; j++) {
                for (int k = 0; k < col; k++) {
                    if (i < len) {

                        mat[j][k] = sentence.charAt(i);
                        i++;
                    }
                }
            }
        }

        i = 0;
        for (int j = 0; j < col; j++) {
            for (int k = 0; k < row; k++) {
                if ((int) mat[k][j] != 0) {
                    System.out.print(mat[k][j]);
                    i++;
                }
            }
            System.out.print(" ");
        }
    }
}