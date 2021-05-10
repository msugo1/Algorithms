/*
   Q: https://programmers.co.kr/learn/courses/30/lessons/12943

   even number: target / 2
   odd number: target * 3 + 1
   - iterate till target reaches 1

   Idea
   1. implement as it is
   2. how can it be optimised further?
   - which led me to this thought. (perhaps 1% better than option no.1)
     1) (even num / 2) can be both odd or even nums
     - no specific rules were found, so I let them be.
     2) (odd num * 3 + 1) will always result in even nums; odd + odd = even, and odd + even = odd
     - odd * 3 is equal to odd + odd + odd, which means even(odd + odd) + odd
     - therefore, the whole result should be even (odd + 1(odd))
     3) now, when odd numbers are stumbled upon, the two process can be done at once. (odd -> even -> ?)
     4) In short, when it is even, follow the normal process, whereas when odd, take two steps simultaneously.
     - a bit of improvement at least!
 */
public class CollatzAssumption {

    public int solution(int num) {
        int maxCount = 500;
        int exeCount = 0;

        long target = num;

        while (target != 1 && exeCount <= maxCount) {
            if (target % 2 == 0) {
                target /= 2;
                exeCount++;
            } else {
                target = (target * 3 + 1) / 2;
                exeCount += 2;
            }
        }

        return exeCount > maxCount ? -1 :exeCount;
    }
}
