// class Eqavg {
//     public static void permute(int[] arr, int k){
//         permuteHelper(arr, 0, k);
//     }
//     private static void permuteHelper(int[] arr, int index, int k){
//         if(index >= arr.length - 1){ //If we are at the last element - nothing left to permute
//             System.out.println(arr);
//             // int sum = 0;
//             // int c1 = 0;
//             // int c2 =0;
//             // for(int i = 0; i < arr.length - k; i++){
//             //     for (int j = i; j < i + k; j++) {
//             //         sum = sum + arr[j];
//             //     }
//             //     c1++;
//             //     double m = sum /k;
//             //     if (sum / k == m) {
//             //         c2++;
//             //     }
//             // }
//             // if (c1 == c2) {
//             //     return c1;
//             // }
//             // return 0;
//         }
//         for(int i = index; i < arr.length; i++){ //For each index in the sub array arr[index...end]
//             //Swap the elements at indices index and i
//             int t = arr[index];
//             arr[index] = arr[i];
//             arr[i] = t;
//             //Recurse on the sub array arr[index+1...end]
//             permuteHelper(arr, index+1, k);
//             //Swap the elements back
//             t = arr[index];
//             arr[index] = arr[i];
//             arr[i] = t;
//         }
//         // return 0;
//     }
//     public static void main(String[] args) {
//         int k = 5;
//         Eqavg.permute(new int[]{1,2,3,4,5}, k);
//     }
// }
class Eqavg {
    public static void permute(int[] arr){
        permuteHelper(arr, 0);
    }
    private static void permuteHelper(int[] arr, int index){
        if(index >= arr.length - 1){ //If we are at the last element - nothing left to permute
            //System.out.println(Arrays.toString(arr));
            //Print the array
            System.out.print(arr);
            // for(int i = 0; i < arr.length - 1; i++){
            //     System.out.print(arr[i] + ", ");
            // }
            // if(arr.length > 0)
            //     System.out.print(arr[arr.length - 1]);
            // System.out.println("]");
            for (int i = 0; i < )
            return;
        }
        for(int i = index; i < arr.length; i++){ //For each index in the sub array arr[index...end]
            //Swap the elements at indices index and i
            int t = arr[index];
            arr[index] = arr[i];
            arr[i] = t;
            //Recurse on the sub array arr[index+1...end]
            permuteHelper(arr, index+1);
            //Swap the elements back
            t = arr[index];
            arr[index] = arr[i];
            arr[i] = t;
        }
    }
    public static void main(String[] args) {
        Eqavg.permute(new int[]{1,2,3,4,5});
    }
}