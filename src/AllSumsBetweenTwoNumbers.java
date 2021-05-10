import java.util.HashMap;
import java.util.Map;

/*
    Q: https://programmers.co.kr/learn/courses/30/lessons/12912

    first try
    - take some modifications onto how to get the sum of 1 ~ n, which is n * (n + 1) / 2
    - n means the number of numbers from the start to the end
    - n + 1 means the sum of the start and the end

    - it should be quicker than just plainly getting values with a for loop but still place a cache for a bit of further improvement.
 */
public class AllSumsBetweenTwoNumbers {

    Map<Integer, Integer> cache = new HashMap<>();

    public long solution(int a, int b) {
        if (a == b) return a;

        int diff = Math.abs(a - b);

        if (cache.get(diff) != null) {
            return cache.get(diff);
        }

        return ((long) diff * (a + b)) / 2;
    }
}
