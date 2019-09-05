import java.util.Scanner; 
import java.util.ArrayList;
import java.util.List;
public class winterishere 
{ 
    static List<List<Integer>> whiteman = new ArrayList<List<Integer>>();
    public static void main(String[] args) 
    { 
        Scanner sc = new Scanner(System.in); 
    
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            List<Integer> row = new ArrayList<Integer>();
            int x = sc.nextInt();
            int y = sc.nextInt();
            row.add(x);
            row.add(y);
            whiteman.add(row);
        }

        int t = sc.nextInt();
        int res = 0;
        for (int i = 0; i < t; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int k = sc.nextInt();
            res = calculatekill(x, y, k);
            System.out.println(res);
        }
        sc.close();
    }

    public static int calculatekill(int x, int y, int k) {
        List<List<Integer>> activewhiteman = new ArrayList<List<Integer>>();
        int kill = 0;
        for (int i = 0; i < whiteman.size(); i++) {
            List<Integer> row2 = new ArrayList<Integer>();
            row2 = whiteman.get(i);

            if (row2.get(0) <= k) {
               activewhiteman.add(row2); 
            }
        }

        for (int i = 0; i < activewhiteman.size(); i++) {
            List<Integer> row3 = new ArrayList<Integer>();
            row3 = whiteman.get(i); 
            int xx = row3.get(2);
            int nfac = factorial(xx);
            kill = kill ^ nfac;
        //     System.out.println("kill::::::::::: ");
        // System.out.println(kill);
        }
        return kill;
        
    } 

    public static int factorial(int num) {
        // System.out.println("num::::::::::: ");
        // System.out.println(num);
        int count = 0;
        for (int i = 2; i < num; i++) {
            if (num % i == 0) {
                count++;
            }
        }
        if (!(num == 1)) {
            count = count + 2;
        } else {
            count++;
        }
        
        // System.out.println("count::::::::::: ");
        // System.out.println(count);
        return count;
    }
} 

