public class PressKeyButtons {

    int[][] locations = {
            {3, 1}, {0, 0}, {0, 1},
            {0, 2}, {1, 0}, {1, 1},
            {1, 2}, {2, 0}, {2, 1},
            {2, 2}
    };

    int[] curr_left = {3, 0};

    int[] curr_right = {3, 2};

    public String solution(int[] numbers, String hand) {
        StringBuilder res = new StringBuilder();

        for (int number : numbers) {
            String usedThumb = pushButton(number, hand);
            res.append(usedThumb);

            if (usedThumb.equals("L")) curr_left = locations[number];
            else curr_right = locations[number];
        }

        return String.valueOf(res);
    }

    private String pushButton(int currNumber, String hand) {
        if (currNumber == 1 || currNumber == 4 || currNumber == 7) return "L";
        if (currNumber == 3 || currNumber == 6 || currNumber == 9) return "R";

        int dist = getDistFromNum(curr_left, currNumber) - getDistFromNum(curr_right, currNumber);
        if (dist > 0) return "R";
        else if (dist < 0) return "L";
        else return hand.equals("right") ? "R" : "L";
    }

    private int getDistFromNum(int[] pos, int currNum) {
        int[] numPos = locations[currNum];
        return Math.abs(pos[0] - numPos[0]) + Math.abs(pos[1] - numPos[1]);
    }
}
