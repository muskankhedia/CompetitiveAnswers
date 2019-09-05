class Result {

    /*
     * Complete the 'getSubsets' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER k
     *  2. INTEGER n
     *  3. INTEGER_ARRAY arr
     */

    public static int getSubsets(int k, int n, List<Integer> arr) {
        int tsum = 0;
        int tsets =0;

        for (int i = 0; i < n ; i++) {
            tsum = tsum + sumPrime(arr.get(i));
        }

        tsets = countP(tsum, k);
        return tsets;


    }

    public static int countP(int n, int k) 
    { 

       if (n == 0 || k == 0 || k > n) 
          return 0; 
       if (k == 1 || k == n) 
          return 1; 
  
       return (k * countP(n - 1, k)  + countP(n - 1, k - 1)); 
    } 

    public static int sumPrime(int number) {
        int sum =0;

        for(int i = 2; i< number; i++) {
         while(number%i == 0) {
            sum = sum + i;
            number = number/i;
         }
      }
      if(number >2) {
         sum = sum + number;
      }
      return sum;

    }
