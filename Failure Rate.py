"""
https://programmers.co.kr/learn/courses/30/lessons/42889
"""

# example
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
# N = 5
import collections
from operator import itemgetter

"""
first try
"""


def first_try(N: int, stages: list) -> list:
    failure_rates = []

    reached_stage_nums = len(stages)
    for level in range(1, N + 1):
        reached_stage_nums -= stages.count(level - 1)
        stuck_stage_nums = stages.count(level)
        failure_rates.append((level, stuck_stage_nums / reached_stage_nums, stuck_stage_nums))

    failure_rates.sort(key=lambda x: (x[1], x[2]), reverse=True)

    return [level[0] for level in failure_rates]


# result - runtime error
# it appears to be time-out. It's probably because count operation in a for loop takes O(N^2)?
# How can the time be reduced?

"""
second try

- change 'list.count' to looking up values from a Counter instance.
- searching values from a hash table takes only O(1), so this should be quicker
"""


def second_try(N: int, stages: list) -> list:
    failure_rates = []

    reached_stage_nums = len(stages)
    people_on_each_stage = collections.Counter(stages)

    for level in range(1, N + 1):
        reached_stage_nums -= people_on_each_stage[level - 1]
        stuck_stage_nums = people_on_each_stage[level]
        failure_rates.append((level, stuck_stage_nums / reached_stage_nums, stuck_stage_nums))

    failure_rates.sort(key=lambda x: (x[1], x[2]), reverse=True)

    return list(map(itemgetter(1), failure_rates))


# result - much faster in runtime as the previous shows the result of even around 2000ms
# but still runtime errors are posed for 8 cases.


"""
third try
"""


def third_try(N: int, stages: list) -> list:
    failure_rates = []

    reached_stage_nums = len(stages)
    people_on_each_stage = collections.Counter(stages)

    for level in range(1, N + 1):
        reached_stage_nums -= people_on_each_stage[level - 1]
        stuck_stage_nums = people_on_each_stage[level]
        failure_rates.append((level, stuck_stage_nums / reached_stage_nums, stuck_stage_nums))

    return list(map(itemgetter(0), sorted(failure_rates, key=lambda x: (x[1], x[2]), reverse=True)))


# It still has the same result. I suppose the for loop must be gone for good

"""
fourth try

the reason was found out with some helps from programmers.
- what posed the runtime error was not actually time-out but when no users challenge a certain stage.

* Two runtime errors that were actually occurring
1. TypeError: 'int' object is not subscriptable won't be raised
2. ZeroDivisionError: division by zero

a few changes from previous logic
- store the failure rate for any stage in a dictionary instead rather than in a tuple
why?
1. ZeroDivision cases are handled thoroughly
2. when the cases above are dealt with, values that are saved are meant to be just integers, which keeps leading to the runtime error 
with key=lambda x: x[1]
- integers are not subscriptable
- dictionaries keys can also be sorted by values
- since the above does not use such operations like [1], the TypeError: 'int' object is not subscriptable won't be raised    
"""


def fourth_try(N: int, stages: list):
    failure_rates = {}

    reached_stage_nums = len(stages)
    people_on_each_stage = collections.Counter(stages)

    for level in range(1, N + 1):
        reached_stage_nums -= people_on_each_stage[level - 1]
        if reached_stage_nums == 0:
            failure_rates[level] = 0
            continue
        stuck_stage_nums = people_on_each_stage[level]
        failure_rates[level] = stuck_stage_nums / reached_stage_nums

    return sorted(failure_rates, key=lambda x: failure_rates[x], reverse=True)