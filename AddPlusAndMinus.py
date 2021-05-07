"""
https://programmers.co.kr/learn/courses/30/lessons/76501
"""

def solution(absolutes, signs):
    answer = []

    for idx, num in enumerate(absolutes):
        if signs[idx]:
            answer.append(num)
        else:
            answer.append(-num)

    return sum(answer)