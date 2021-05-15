"""
https://programmers.co.kr/learn/courses/30/lessons/77484
"""

"""
first try

logic
- the number of 0s seems to play a huge role here.
- break these into three cases: all 6 as 0, no 0, and the rest

1. all are zeros
- it can be either 1st or 6th
2. none is zero
- winning numbers that are originally in the given list will determine its destiny.
3. the rest
- winning numbers should take the lowest case, whereas winning numbers combined the number of zeros
will lead to the highest 
"""


def solution(lottos: list, win_nums: list):
    zero_count = lottos.count(0)

    if zero_count == len(win_nums):
        return 1, 6

    win_num_count = 0
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    for each_num in lottos:
        if each_num in win_nums:
            win_num_count += 1

    if zero_count == 0:
        return rank.get(win_num_count), rank.get(win_num_count)

    return rank.get(win_num_count + zero_count), rank.get(win_num_count)


lotto = [44, 1, 0, 0, 31, 25]
win = [31, 10, 45, 1, 6, 19]
