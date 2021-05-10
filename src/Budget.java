import java.util.Arrays;

/*
    idea: sort the array and hand out the budget from the lowest ones. (greedy but as the opposite)
 */
public class Budget {

    public int solution(int[] d, int budget) {
        int answer = 0;
        Arrays.sort(d);

        for (int requestedBudget : d) {
            if (requestedBudget > budget)
                break;

            budget -= requestedBudget;
            answer++;
        }

        return answer;
    }
}
