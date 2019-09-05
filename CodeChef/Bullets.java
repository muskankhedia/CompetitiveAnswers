import java.util.Scanner;
import java.util.List;
import java.lang.*;
class Bullets
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int p = sc.nextInt();
            String input = sc.nextLine();
            String[] numbersStr = input.split(" ");
            int[] numbers = new int[ numbersStr.length ];

            for ( int j = 0; j < numbersStr.length; j++ )
            {
                numbers[j] = Integer.parseInt( numbersStr[j] );
                System.out.print( numbers[j] + ", " );
            }
            System.out.println();

        }

    }
}