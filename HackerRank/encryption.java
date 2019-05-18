import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.math.*;

public class encryption {
    public static final Scanner sc = new Scanner(System.in);

    public static ArrayList<String> breakDown(String s, int rows, int columns) {
        // System.out.println(s+" "+rows+" "+columns);
        ArrayList<String> temp = new ArrayList<String>();
        int last = 0;
        while(true) {
            try {
            temp.add(s.substring(last, last + columns));
            last += columns;
            } catch(Exception e) {
                temp.add(s.substring(last, s.length()));
                break;
            }
        }
        temp.removeAll(Arrays.asList(null,""));
        return temp;
    }

    private static String filter(String a) {
        String temp = "";
        for(int i=0; i<a.length(); i++) {
            if (!(a.charAt(i) == ' ')) {
                temp += a.charAt(i);
            }
        }
        return temp;
    }
    public static void main(String[] args) {
        String s = sc.nextLine();
        s = filter(s);
        int size = s.length();
        // System.out.println(size);
        double root = Math.sqrt(size);
        int ceil = (int) Math.ceil(root), floor = (int) Math.floor(root);
        int[][] possibilities_rc = new int[1][2];
        possibilities_rc[0][0] = floor;
        possibilities_rc[0][1] = ceil;

        // possibilities_rc[1][0] = floor;
        // possibilities_rc[1][1] = floor;
        int min = 10000;
        String answer = "";
        for(int i=0; i< possibilities_rc.length; i++) {
            if (
                floor <= possibilities_rc[i][0] 
                && possibilities_rc[i][0] <= possibilities_rc[i][1] 
                && possibilities_rc[i][1] <= ceil
                // && (possibilities_rc[i][0] * possibilities_rc[i][1] <= size)
                && (min > (possibilities_rc[i][0] * possibilities_rc[i][1]))) {
                answer = "";
                ArrayList<String> a = breakDown(s, possibilities_rc[i][0], possibilities_rc[i][1]);
                // System.out.println(a);
                min = possibilities_rc[i][0] * possibilities_rc[i][1];
                for(int j=0 ; j< possibilities_rc[i][1]; j++) {
                    for(int k=0; k< a.size(); k++) {
                        try {
                        answer += a.get(k).charAt(j);
                        } catch(Exception e) {
                            continue;
                        }
                    }
                    answer += " ";
                }
            } 
        }
        System.out.println(answer);
    }
}
