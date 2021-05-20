"""
    Q: https://programmers.co.kr/learn/courses/30/lessons/12985

    Idea
    - At every step to the next stage, its current number gets divided by 2 (like log 2) 
        : being an even or odd number holds a different equation, which can be offset by adding + 1 to the original number before being divided
        (why? it will make an odd number an even one, and an even number an odd number, which will have the same quotient
         with the same equation that would be meant to have otherwise with different equations depending on the cases)
    - recursively proceed to the next match or return the round where both finally confront each other.
        : to do so, count should be incremented on each round.
    - both being met means the even one's number is only positive one apart from the odd one's
"""


def solution(n, a, b):
    starting_count = 1

    return proceed_match(starting_count, a, b)


def proceed_match(count, participant_1, participant_2):
    condition_1 = (participant_2 % 2 == 0) and (participant_2 - participant_1 == 1)
    condition_2 = (participant_1 % 2 == 0) and (participant_1 - participant_2 == 1)

    if condition_1 or condition_2:
        return count

    return proceed_match(count + 1, (participant_1 + 1) // 2, (participant_2 + 1) // 2)
