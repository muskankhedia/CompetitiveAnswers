import java.util.Scanner;

public class queen2 {

    private static Integer attackingPlaces(int[][] board, int r_q, int c_q, int[][] obstacles, int n) {
        int count = 0;
        // for(int obs = 0; obs < obstacles.length; obs++) {
            // left
            for(int i=c_q-1; i>=1; i--) {
                if (board[r_q][i] != 1 && board[r_q][i] != 2)
                    {count++;}
                else if (board[i][c_q] != 1) {count++; break;}
                else break;
            }

            // right
            for(int i=c_q+1; i<=n; i++) {
                if (board[r_q][i] != 1 && board[r_q][i] != 2)
                    {count++;}
                else if (board[i][c_q] != 1) {count++; break;}
                else break;
            }

            // up
            for(int i=r_q+1; i<=n; i++) {
                if (board[i][c_q] != 1 && board[i][c_q] != 2)
                    {count++;}
                else if (board[i][c_q] != 1) {count++; break;}
                else break;
            }

            // down
            for(int i=c_q-1; i>1; i--) {
                if (board[i][c_q] != 1 && board[i][c_q] != 2)
                    {count++;}
                else if (board[i][c_q] != 1) {count++; break;}
                else break;
            }

            // cross left to right
            for(int i=r_q,j=c_q; i<=n && j<=n; i++, j++) {
                // for(int j=c_q; j<n; j++) {
                    if (i == r_q && j == c_q) 
                        continue;
                    if (board[i][j] != 1 && board[i][j] != 2)
                        {count++;}
                    else if (board[i][c_q] != 1) {count++; break;}
                    else break;
                // }
            }
            for(int i = r_q,j=c_q; i>=1 && j>=1; i--, j--) {
                // for(int  j>=0; j--) {
                    if (i == r_q && j == c_q) 
                        continue;
                    if (board[i][j] != 1 && board[i][j] != 2)
                        {count++;}
                    else if (board[i][c_q] != 1) {count++; break;}
                    else break;
                // }
            }

            // cross right to left
            for(int i=r_q,j=c_q; i<=n && j>=1; i++, j--) {
                // for(int j=c_q; j>=0; j--) {
                    if (i == r_q && j == c_q) 
                        continue;
                    if (board[i][j] != 1 && board[i][j] != 2)
                        {count++;}
                    else if (board[i][c_q] != 1) {count++; break;}
                    else break;
                // }
            }
            for(int i = r_q, j=c_q; i>=1 && j<=n; i--, j++) {
                // for(int j=c_q; j<n; j++) {
                    if (i == r_q && j == c_q) 
                        continue;
                    if (board[i][j] != 1 && board[i][j] != 2)
                        {count++;}
                    else if (board[i][c_q] != 1) {count++; break;}
                    else break;
                // }
            }
        // }
        return count;
        
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), k = sc.nextInt(), r_q = sc.nextInt(), c_q = sc.nextInt();
        int[][] board = new int[n+1][n+1];
        int[][] obstacles = new int[k+1][2];
        for(int i=1; i<=n; i++) {
            for(int j=1; j<=n; j++) {
                board[i][j] = 0;
            }
        }
        r_q = n +1 -r_q;
        c_q = n+1 - c_q;
        board[r_q][c_q] = 2;
        for(int i=1; i<=k; i++) {
            // System.out.println("here");
            obstacles[i][0] = n +1 -sc.nextInt(); // row
            obstacles[i][1] =n +1 -sc.nextInt(); // column
            board[obstacles[i][0]][obstacles[i][1]] = 1;
        }
        // for(int i=1; i<=n; i++) {
        //     for(int j=1; j<=n; j++) {
        //         System.out.print(board[i][j]);
        //     }
        //     System.out.println();
        // }

        System.out.println( attackingPlaces(board, r_q, c_q, obstacles, n));

    }
}