import java.util.Arrays;

/*
    Q: https://programmers.co.kr/learn/courses/30/lessons/12922

    process
    1. return "수" when n is 1, and "수박" when n is 2
    2. other cases see this case, repeating "수박" for (the entire number / 2) times, and add "수" if rest is not 0
 */
public class RepeatingLetters {

    public String solution(int n) {
        String one = "수";
        String two = "수박";

        if (n == 1) return one;
        if (n == 2) return two;

        StringBuilder res = new StringBuilder();
        res.append(two.repeat(n / 2));
        if ((n % 2) == 1) res.append(one);

        return String.valueOf(res);
    }

    // 65 ~ 90 ASCII A-Z 26개
    // 97 ~ 122 ASCII a-z
    public static void main(String[] args) {
        String pwd = "ab";
        int moving = 50;
        char[] chars = pwd.toCharArray();

        for (int i = 0; i < chars.length; i++) {
            char temp = chars[i];
            if (temp != 32) chars[i] += moving;
            chars[i] = moveBackIfNecessary(temp, chars[i]);
        }

        System.out.println(Arrays.toString(chars));

    }

    private static char moveBackIfNecessary(int prev, int curr) {
        int upperCaseUpperBoundary = 90;
        int upperCaseLowerBoundary = 64;
        int lowerCaseLowerBoundary = 96;
        int lowerCaseUpperBoundary = 122;

        if (prev <= upperCaseUpperBoundary && upperCaseUpperBoundary < curr) {
            return (char) (curr - upperCaseUpperBoundary + upperCaseLowerBoundary);
        } else if (lowerCaseLowerBoundary <= prev && lowerCaseUpperBoundary < curr) {
            return (char) (curr - lowerCaseUpperBoundary + lowerCaseLowerBoundary);
        } else {
            return (char) curr;
        }
    }
}
