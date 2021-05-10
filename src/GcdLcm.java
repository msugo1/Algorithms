import java.util.Arrays;

/*
    Q: https://programmers.co.kr/learn/courses/30/lessons/12940

    Idea: Euclidean algorithm

    * GCP
    1. divide the bigger one by smaller one
    2. After the operation, the remainder becomes a new divisor, and the original divisor, a new dividend.
    3. repeat the same process till it gives you 0 as a remainder.
    4. what makes the remainder zero (the last divisor) is the GCD.

    * LCM
    - two numbers consist of a certain number multiplied by their GCD
    ex. A = aG, B = bG
    - LCM is acquired by multiplying GCD by with the other two certain numbers
    ex. a * b * G

    1. A * B yields the result, a * b * G^2
    2. divide it by their GCD
    = A * B / GCD = a * b * GCD

    Euclidean algorithm can be achieved by both iteration and recursion.
 */
public class GcdLcm {

    public int[] solution_iteration(int n, int m) {
        int dividend = Math.max(n, m);
        int divisor = Math.min(n, m);

        while (divisor > 0) {
            int temp = divisor;
            divisor = dividend % divisor;
            dividend = temp;
        }

        return new int[] {dividend, n * m / dividend};
    }

    public int[] solution_recursion(int n, int m) {
        int big = Math.max(n, m);
        int small = Math.min(n, m);

        int gcd = calculateGCD(big, small);
        return new int[] {gcd, big * small / gcd};
    }

    /*
        this method will be executed recursively up to which GCD will be returned.
     */
    public int calculateGCD(int big, int small) {
        if (big % small == 0) {
            return small;
        }

        return calculateGCD(small, big % small);
    }
}
