import re

"""
https://programmers.co.kr/learn/courses/30/lessons/72410
"""


#     special_character_pattern = re.compile(r"[~!@#$%^&*()=+\[{\]}:?,<>/]")
#     too_many_dots_pattern = re.compile(r"\.{2,}")
#     dots_on_ends_pattern = re.compile(r"^\.|\.$")
"""
first try
- use a regular expression to filter out letters out of boundary
- then check other extra conditions and take modification

result
- fail for the case with "abcdefghijklmn.p"
- need to fix the logic
    : the process has to be done multiple times
"""


def solution(new_id):
    upper_bound = 15
    lower_bound = 3

    target_id = new_id

    step_one_two = remove_unexpected_chars(target_id)
    step_three = remove_repetitive_dots(step_one_two)
    target_id = remove_dots_on_ends(step_three)

    if target_id == "":
        target_id += "a"

    if len(target_id) > upper_bound:
        target_id = target_id[:upper_bound]
    elif len(target_id) < lower_bound:
        while len(target_id) < lower_bound:
            target_id += target_id[-1]

    return target_id


def remove_unexpected_chars(user_id):
    return re.sub(r"[~!@#$%^&*()=+\[{\]}:?,<>/]", "", user_id.lower())


def remove_repetitive_dots(user_id):
    return re.sub(r"\.{2,}", ".", user_id)


def remove_dots_on_ends(user_id):
    return re.sub(r"^\.|\.$", '', user_id)


new_id = "abcdefghijklmn.p"
print(solution(new_id))
