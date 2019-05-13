
import java.io.*;
import java.util.ArrayList;
import java.util.Random;

public class nondivisiblesubsets {

    public ArrayList<Integer> generateSubset(int[] s, int n) {
        Random rand = new Random();
        int size = s.length;
        ArrayList<Integer> tempArr = new ArrayList<Integer>();
        for(int i=0; i< n; i++) {
            tempArr.add(rand.nextInt(size));
        }
        return tempArr;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()), k = Integer.parseInt(br.readLine());
        int temp = 0, set[] = new int[n], c =0;
        while(temp++ != n) {
            set[temp] = Integer.parseInt(br.readLine());
            if (set[temp] % 3 == 0) 
                c++;    
        }

    }
}