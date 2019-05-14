
import java.io.*;
import java.util.ArrayList;
import java.util.Random;

public class nondivisiblesubsets {

    public static ArrayList<Integer> generateSubset(int[] s, int n) {
        Random rand = new Random();
        int size = s.length;
        ArrayList<Integer> tempArr = new ArrayList<Integer>();
        for(int i=0; i< n; i++) {
            tempArr.add(rand.nextInt(size));
        }
        return tempArr;
    }

    public static Boolean checkSumDivByk(ArrayList<Integer> s, int k) {
        System.out.println("s is " + s);
        int size = s.size(), sum=0;
        for(int i=0; i<size; i++) {
            for(int j=i+1; j<size; j++) {
                sum = s.get(i) + s.get(j);
                if (sum % k == 0){
                    System.out.println("a yes at " + Integer.toString(sum)+ " of "+ Integer.toString(s.get(i)
                    ) + "  + "+ Integer.toString(s.get(i)));
                    return true;
                }
            }
        }
        return false;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()), k = Integer.parseInt(br.readLine());
        int temp = 0, set[] = new int[n];
        for(temp = 0; temp < n; temp ++) { // taking inputs
            set[temp] = Integer.parseInt(br.readLine());
        }
        System.out.println("outputs below");
        temp = 0;
        int max =0;
        for (int i =2; i<=n; i++) {
            for(int j=0; j<n; j++) {
                ArrayList<Integer> arList = generateSubset(set, i);
                if (checkSumDivByk(arList, k)) {
                    int len = arList.size();
                    max = len > max ? len : max;
                }
            }
        }
        System.out.println(max);

    }
}