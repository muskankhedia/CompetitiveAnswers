
import java.io.*;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class nondivisiblesubsets {
    static Random rand;

    public static ArrayList<Integer> generateSubset(int[] s, int n) {
        rand = new Random();
        int size = s.length;
        ArrayList<Integer> tempArr = new ArrayList<Integer>();
        for(int i=0; i< n; i++) {
            int temp = rand.nextInt(size);
            boolean found = false;
            for(int k =0; k< tempArr.size(); k++) {
                if (tempArr.get(k) == s[temp]) 
                    found = true;
            }
            if (!found)
                tempArr.add(s[temp]);
            else 
                n += 1;
        }
        return tempArr;
    }

    public static Boolean checkSumDivByk(ArrayList<Integer> s, int k) {
        int size = s.size(), sum=0;
        for(int i=0; i<size; i++) {
            for(int j=i+1; j<size; j++) {
                sum = s.get(i) + s.get(j);
                if (sum % k == 0){
                    return true;
                }
            }
        }
        return false;
    }
    public static void main(String[] args) throws IOException {
        Scanner br = new Scanner(System.in);
        int n = br.nextInt(), k = br.nextInt();
        int temp = 0, set[] = new int[n];
        for(temp = 0; temp < n; temp ++) { // taking inputs
            set[temp] = br.nextInt();
        }
        temp = 0;
        int max =0;
        for (int i =2; i<=n; i++) {
            for(int j=0; j<n*n; j++) {
                ArrayList<Integer> arList = generateSubset(set, i);
                if (!checkSumDivByk(arList, k)) {
                    int len = arList.size();
                    max = len > max ? len : max;
                }
            }
        }
        System.out.println(max);
        br.close();
    }
}
