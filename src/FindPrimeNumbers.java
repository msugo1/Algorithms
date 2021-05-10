import java.util.ArrayList;
import java.util.List;

/*
    Q: https://programmers.co.kr/learn/courses/30/lessons/12921

    process
    - so far, everything that has been come up with is related to double for loops only.
    - however, iterating up to just sqrt(targetNumber) other than from 2 to the targetNumber entirely hopefully reduces some overheads at least.
 */
public class FindPrimeNumbers {

    public int solution(int n) {
        List<Integer> primes = new ArrayList<>();

        for (int num = 2; num <= n; num++) {
            int upperBound = (int) (Math.sqrt(num) + 1);
            for (int divisor = 2; divisor <= upperBound; divisor++) {
                if (num != divisor && num % divisor == 0) break;
                if (upperBound == divisor) primes.add(num);
            }
        }

        return primes.size();
    }

/*
    - It can't meet my expectations obviously with O(n^2) time complexity.
    - I wouldn't have wondered even with time out errors any time soon.
    - Would there be any way that's more efficient than double iteration.
 */

    public int primeNumberSieve(int n) {
        int[] sieve = initializeSieve(n);

        for (int i = 2; i <= n; i++) {
            if (sieve[i] == 0) continue;

            for (int j = i * 2; j < n; j += i) {
                sieve[j] = 0;
            }
        }

        return sieve.length;
    }


    public int[] initializeSieve(int n) {
        int[] sieve = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            sieve[i] = i;
        }

        return sieve;
    }
}

