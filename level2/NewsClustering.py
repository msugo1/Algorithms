import collections
import math


"""
    Q: https://programmers.co.kr/learn/courses/30/lessons/17677
    
    idea
    1. create a list of subsets with elements comprised of each 2 letters.
    2. count their numbers - dictionary would do
    3. get an intersect and union of them. 
        - intersect: common, and lower nums for any duplicate elements
        - union: any, and bigger nums for duplicate ones
    4. calculate the similarity with the given equation.
"""


def solution(str1, str2):
    value_to_be_multiplied = 65536

    if str1.lower() == str2.lower():
        return 1 * value_to_be_multiplied

    if len(str1) == 0 and len(str2) == 0:
        return 1 * value_to_be_multiplied

    ms1 = str_to_multiple_sets(str1)
    ms2 = str_to_multiple_sets(str2)

    ms1_counts = collections.Counter(ms1)
    ms2_counts = collections.Counter(ms2)

    ms_intersect = (ms1_counts & ms2_counts)
    ms_union = (ms1_counts | ms2_counts)

    return math.floor(sum(ms_intersect.values()) / sum(ms_union.values()) * value_to_be_multiplied)


def str_to_multiple_sets(given_string):
    length = 2
    return [given_string[i:i + length].lower() for i in range(0, len(given_string) - 1) if
            given_string[i:i + length].isalpha()]