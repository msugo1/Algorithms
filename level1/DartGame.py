import re
"""
https://programmers.co.kr/learn/courses/30/lessons/17682
"""

"""
first try
"""


def solution(dart_result: str) -> int:
    score_per_round = []
    idx = 0

    while idx < len(dart_result):
        if dart_result[idx].isdigit() and dart_result[idx + 1].isdigit():
            current_round_score = calculate_current_round_score(dart_result[idx:idx + 2], dart_result[idx + 2])
            score_per_round.append(current_round_score)
            idx += 3
        elif dart_result[idx].isdigit() and dart_result[idx + 1].isdigit() is False:
            current_round_score = calculate_current_round_score(dart_result[idx], dart_result[idx + 1])
            score_per_round.append(current_round_score)
            idx += 2
        else:
            apply_option(score_per_round, dart_result[idx])
            idx += 1

    return sum(score_per_round)


def calculate_current_round_score(score: str, bonus: str) -> int:
    power = 0

    if bonus == "S":
        power = 1
    elif bonus == "D":
        power = 2
    elif bonus == "T":
        power = 3

    return pow(int(score), power)


def apply_option(scores: list, option: str):
    length = len(scores)

    if length == 1:
        if option == "*":
            scores[length - 1] *= 2
        else:
            scores[length - 1] *= -1
    else:
        if option == "*":
            scores[length - 1] *= 2
            scores[length - 2] *= 2
        else:
            scores[length - 1] *= -1


result = "1D2S#10S"
