import java.util.Random;

public class java_gen {
    public static void main(String[] args) 
    {
        Random random = new Random();
        int length = 128;

        StringBuilder binarySeq = new StringBuilder(length);
        for (int i = 0; i < length; i++) 
        {

            int bit = random.nextInt(2);
            binarySeq.append(bit);
        }

        System.out.println("Random sequence: " +binarySeq.toString());
    }
}