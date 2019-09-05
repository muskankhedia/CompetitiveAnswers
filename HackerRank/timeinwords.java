import java.util.Scanner;
import java.util.ArrayList;

public class timeinwords {
    private static final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int h = sc.nextInt();
        while(h-- != 0) {
            String s = sc.nextLine();
            int colonIndex = s.indexOf(":");
            int hrs = Integer.parseInt(s.substring(0, colonIndex));
            int mins = Integer.parseInt(s.substring(colonIndex+1));
            
        }
    }
}