import java.util.Locale;

/*
   Q: https://programmers.co.kr/learn/courses/30/lessons/12930#
 */
public class MakeWeirdStrings {


    /*
       Step
       1. split the given strings based on the blank " "
       2. iterate the String array created by the split method.
       - Meanwhile, turn each string into a char Array, make any char on specific indices upper or lower cases with another loop.
       3. transform the modified char characters into a String, and then let it replace the original string before the modification.
       4. join all together in one string with the original blank " "

       Learned on the way
       - split can have a limit argument. (-1 appears to act as excluding the end)

       Inefficiency
       - double for loops in this code.
     */
    public String solution(String s) {
        String[] strings = s.split(" ", -1);

        for (int i = 0; i < strings.length; i++) {
            char[] chars = strings[i].toCharArray();

            for (int j = 0; j < chars.length; j++) {
                if (j % 2 == 0) chars[j] = Character.toUpperCase(chars[j]);
                else chars[j] = Character.toLowerCase(chars[j]);
            }
            strings[i] = new String(chars);
        }

        return String.join(" ", strings);
    }

    /*
        a Solution from Programmers
        1. sort the inefficiency out by splitting the given string based on ""
        - "" means split each and every single letter including blanks, " "
        2. then count the current location
        - turn count back to 0 if it is a blank that has been run into at a loop. (equivalent to marking a new string)
        - if not, increment the 'count' count.
        3. Note that the count variable is meant to start from 1, meaning that toUpperCase has to be applied to elements on odd indices,
        and toLowerCase to even ones. (unlike how the question describes the requirements as that begins from 0)
     */
    public String secondSolution(String s) {
        String[] strings = s.split("");

        int count = 0;
        StringBuilder sb = new StringBuilder();
        for (String string : strings) {
            count = string.contains(" ") ? 0 : ++count;
            if (count % 2 == 0) sb.append(string.toLowerCase());
            else sb.append(string.toUpperCase());
        }

        return sb.toString();
    }
}
