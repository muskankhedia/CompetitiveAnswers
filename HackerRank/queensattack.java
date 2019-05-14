import java.util.Scanner;

public class queensattack {

    private static Integer attackingPlaces(int[][] board, int r_q, int c_q, int[][] obstacles, int n) {
        int count = 0;
        // for(int obs = 0; obs < obstacles.length; obs++) {
            // left
            for(int i=c_q-1; i>=0; i--) {
                if (board[r_q][i] != 1 && board[r_q][i] != -1)
                    count++;
                else break;
            }

            // right
            for(int i=c_q+1; i<n; i++) {
                if (board[r_q][i] != 1 && board[r_q][i] != -1)
                    count++;
                else break;
            }

            // up
            for(int i=r_q+1; i<n; i++) {
                if (board[i][c_q] != 1 && board[i][c_q] != -1)
                    count++;
                else break;
            }

            // down
            for(int i=c_q-1; i>=0; i--) {
                if (board[i][c_q] != 1 && board[i][c_q] != -1)
                    count++;
                else break;
            }

            // cross left to right
            for(int i=r_q; i<n; i++) {
                for(int j=c_q; j<n; j++) {
                    if (i == r_q && j == c_q) 
                        continue;
                    if (board[i][j] != 1 && board[i][j] != -1)
                        count++;
                }
            }
            for(int i = r_q; i>=0; i--) {
                for(int j=c_q; j>=0; j--) {
                    if (i == r_q && j == c_q) 
                        continue;
                    if (board[i][j] != 1 && board[i][j] != -1)
                        count++;
                }
            }

            // cross right to left
            for(int i=r_q; i<n; i++) {
                for(int j=c_q; j>=0; j--) {
                    if (i == r_q && j == c_q) 
                        continue;
                    if (board[i][j] != 1 && board[i][j] != -1)
                        count++;
                }
            }
            for(int i = r_q; i>0; i--) {
                for(int j=c_q; j<n; j++) {
                    if (i == r_q && j == c_q) 
                        continue;
                    if (board[i][j] != 1 && board[i][j] != -1)
                        count++;
                }
            }
        // }
        return count;
        
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), k = sc.nextInt(), r_q = sc.nextInt(), c_q = sc.nextInt();
        r_q -= 1;
        c_q -= 1;
        int[][] board = new int[n][n];
        int[][] obstacles = new int[k][2];
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                board[i][j] = 0;
            }
        }
        board[r_q][c_q] = -1;
        for(int i=0; i< k; i++) {
            obstacles[i][0] = sc.nextInt(); // row
            obstacles[i][1] = sc.nextInt(); // column
            obstacles[i][1] -= 1;
            obstacles[i][0] -= 1;
            board[obstacles[i][0]][obstacles[i][1]] = 1;
        }
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                System.out.print(board[i][j]);
            }
            System.out.println();
        }

        System.out.println( attackingPlaces(board, r_q, c_q, obstacles, n));

    }
}