import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {


    static int[] arr = new int[100000];

    public static void cal() {

        arr[0] = 0;
        arr[1] = 1;
        for (int x = 0; x < 10000; x++) {
            long a = x % 8;
            if(a == 0 || a == 1) {
                arr[x] = x;
            }
            if(a == 2 || a == 3) {
                arr[x] = 2;
            }
            if(a == 4 || a == 5) {
                arr[x] = x + 2;
            }
            if(a == 6 || a == 7) {
                arr[x] = 0;
            }

        }
    }

    // Complete the xorSequence function below.
    static long xorSequence(long l, long r) {
        long res = 0;
        for (long j = l; j <= r; j++) {
            int c = (int)j;
            res = res ^ arr[c];
        }
        return res;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
        cal();

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String[] lr = scanner.nextLine().split(" ");

            long l = Long.parseLong(lr[0]);

            long r = Long.parseLong(lr[1]);

            long result = xorSequence(l, r);

            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
