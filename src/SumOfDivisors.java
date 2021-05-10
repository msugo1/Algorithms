import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/*
    https://programmers.co.kr/learn/courses/30/lessons/12928

    two ideas that's come to the mind.

    1. iterate in a for loop from one to a certain N number.
        - in the meantime, check if n % (curr number) is equal to 0
        - if so, put it somewhere like an array or List

    2. implement a code that makes use of the equation that calculates the sum of divisors for a certain N number.

    Here, the second option is chosen because the first is not as hard a nut to crack.
 */
public class SumOfDivisors {

    Map<Integer, Integer> powers = new HashMap<>();

    public int solution(int n) {
        int divisor = 2;

        while (n >= divisor) {
            if (n % divisor != 0) {
                divisor++;
                continue;
            }
            powers.compute(divisor, (k, v) -> v == null ? 1 : v + 1);
            n /= divisor;
        }

        return calculateDivisorSums();
    }

    private int calculateDivisorSums() {
        int ans = 1;
        Set<Map.Entry<Integer, Integer>> entries = powers.entrySet();

        for (Map.Entry<Integer, Integer> entry : entries) {
            ans *= (int) ((Math.pow(entry.getKey(), entry.getValue() + 1) - 1) / (entry.getKey() - 1));
        }

        return ans;

    }

    public static void main(String[] args) {
        SumOfDivisors divisors = new SumOfDivisors();
        System.out.println(divisors.solution(12));
    }
}
