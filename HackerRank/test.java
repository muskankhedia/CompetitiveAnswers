import java.util.Random;

public class test {
    public static void main(String[] args) {
        Random rand = new Random();
        int n = 100;
        while (n-- != 0) {
            System.out.println(rand.nextInt(10));
        }
    }
}