"""
    Q: https://programmers.co.kr/learn/courses/30/lessons/60058

    idea
        1. find an index that divides the given string into two parts. (described as u, v in an explanation)
        2. separate the given string with the calculated index.
        3. two cases should be handled individually (correct brackets, and not correct but at least balanced ones.)
            However, it actually turned out that all cases that starts with "(" comes to the first, whereas the other to the second,
            which facilitates this question a lot more.
        4.
            1) correct brackets: return u concatenated with v that goes through the 1 ~ 3 process once more. (the u part will be left untouched.)
            2) balanced brackets
                (1) wrap the v part processed in recursion around with brackets
                (2) the u part needs to ditch the brackets on its first and last indices, followed by it being reversed.
                (3) return the result: (1) and (2) concatenated
"""


def solution(p):
    # base_case
    if p == "":
        return ""

    # recursive_case
    division_point = find_point_for_division(p)

    u = p[:division_point]
    v = p[division_point:]

    if p[0] == "(":
        return u + solution(v)
    else:
        temp = "(" + solution(v) + ")"
        u = u[1: len(u) - 1]
        reversed_u = reverse(u)
        return temp + reversed_u


def find_point_for_division(given_string):
    idx, open_count, close_count = 0, 0, 0

    for each_letter in given_string:
        idx += 1
        if each_letter == "(":
            open_count += 1
        else:
            close_count += 1

        if open_count == close_count:
            break

    return idx


def reverse(given_string):
    r = {"(": ")", ")": "("}
    return ''.join([r[s] for s in given_string])