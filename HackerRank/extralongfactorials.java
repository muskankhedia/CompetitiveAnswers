/**
 * 
 * https://www.hackerrank.com/challenges/extra-long-factorials/problem
 * 
 */

import java.util.Scanner;
import java.math.*;

public class extralongfactorials {
    public static void main(String[] args) {
        BigInteger big = new BigInteger("1");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i =1; i<=n; i++) {
            BigInteger a = new BigInteger(Integer.toString(i));
            big = big.multiply(a);
        }
        System.out.println(big);
        sc.close();
    }
}
