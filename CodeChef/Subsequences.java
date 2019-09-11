import java.util.ArrayList;
import java.util.Scanner;

public class Subsequences {

	public static int min = 10000;
	public static int sum = 0, count = 0;

	public void subset(int[] A, int k, int start, int currLen, boolean[] used) {

		if (currLen == k) {
			ArrayList<Integer> al=new ArrayList<Integer>();
			sum = 0;
			for (int i = 0; i < A.length; i++) {
				if (used[i] == true) {
					// System.out.print(A[i] + " ");
					al.add(A[i]);
				}
			}
			for(int i = 0; i < al.size(); i++)
				sum += al.get(i);
			
			if (sum < min) {
				min = sum;
				count = 1;
			} else if (sum == min) {
				count++;
			}
			// System.out.println();
			return;
		}
		if (start == A.length) {
			return;
		}
		// For every index we have two options,
		// 1.. Either we select it, means put true in used[] and make currLen+1
		used[start] = true;
		subset(A, k, start + 1, currLen + 1, used);
		// 2.. OR we dont select it, means put false in used[] and dont increase
		// currLen
		used[start] = false;
		subset(A, k, start + 1, currLen, used);
	}

	public static void main(String[] args) {
		int n, k, t;
		Scanner Sc = new Scanner(System.in);
		t = Sc.nextInt();
		while (t > 0) {
			n = Sc.nextInt();
			k = Sc.nextInt();
			int[] A = new int[n];
			for (int i=0; i< n; i++) {
				A[i] = Sc.nextInt();
			}
			// int A[] = { 1, 2, 3, 4, 5 };
			boolean[] B = new boolean[A.length];
			Subsequences i = new Subsequences();
			i.subset(A, k, 0, 0, B);
			System.out.println(count); 
			t--;
		}
		
		Sc.close();

	}

}