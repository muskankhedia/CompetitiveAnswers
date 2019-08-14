import java.util.Scanner;
import java.util.ArrayList;

public class lexicographical {
    private static final Scanner sc = new Scanner(System.in);

    private static Integer factorial(int n) {
        int p=1;
        for(int i=1; i<=n; i++) {
            p *= i;
        }
        return p;
    }
    public static void main(String[] args) {
        int t = sc.nextInt();
        while(t-- != 0) {
            String s = sc.nextLine();
            int size = s.length();
            char last = s.charAt(size-1);
        }
    }
}