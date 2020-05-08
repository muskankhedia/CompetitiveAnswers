import java.util.Scanner;

import sun.security.util.Length;

import java.util.Arrays;

public class Bey {
    public static void main(String[] args) {
        int t, n, sum = 0;
        Scanner s = new Scanner(System.in);
        t = s.nextInt();
        while (t > 0) {
            t--;
            n = s.nextInt();
            int TeamG[] = new int[n];
            int TeamO[] = new int[n];
            for (int i = 0; i < n; i++) {
                TeamG[i] = s.nextInt();
            }
            for (int i = 0; i < n; i++) {
                TeamO[i] = s.nextInt();
            }

            Arrays.sort(TeamG);
            Arrays.sort(TeamO);

            int win_counts = 0;

            for (int i = 0; i < TeamO.length; i++) {
                for (int j = 0; j < TeamG.length; j++) {
                    if (TeamG[j] > TeamO[i]) {
                        for(int k = j; k < TeamG.length -1; k++){
                            TeamG[k] = TeamG[k + 1];
                          }
                          win_counts += 1;
                    }
                }
            }
            System.out.println(win_counts);
        }

    }
}