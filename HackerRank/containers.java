import java.util.Scanner;

public class containers {
    public static final Scanner sc = new Scanner(System.in);

    public static void doprocess(int[][] containerAll, int n) {
        int[] capacityContainer = new int[n];
        for(int i=0; i<n; i++) {
            capacityContainer[i] = 0;
            for(int j=0; j<n; j++) {
                capacityContainer[i] += containerAll[i][j];
            }
        }
        int[] amountEachBall = new int[n];
        for(int i=0; i<n; i++) {
            amountEachBall[i] = 0;
            for(int j=0; j<n; j++) {
                amountEachBall[i] += containerAll[j][i];
            }
        }
        boolean found = false;
        for(int i=0; i< n; i++) {
            for(int j=0;j <n; j++) {
                if (amountEachBall[j] == capacityContainer[i]) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                System.out.println("Impossible");
                break;
            }
            else if (i == n-1)
                System.out.println("Possible");
        }
    }
    public static void main(String[] args) {
        int q = sc.nextInt();
        for(int m=1; m<=q; m++) {
            int n = sc.nextInt();
            int[][] containerAll = new int[n][n];
            //inputs
            for(int i=0; i<n; i++) {
                for(int j=0; j<n; j++) {
                    containerAll[i][j] = sc.nextInt();
                }
            }
            doprocess(containerAll, n);
        }
    }
}