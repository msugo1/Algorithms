import collections
from typing import Dict

"""
Q. find a participant that does not finish the marathon.

example: 
- participants = ["mislav", "stanko", "mislav", "ana"]
- completions = ["stanko", "ana", "mislav"]

A: it is one 'mislav' as one is not in completions.
"""

"""
first try 
 
logic
1. convert the given lists to dictionaries
- add 1 to values 
    if their keys already have them 
    else set values as 1 
2. then compare the values with keys from the dictionary based on the participant list
- any key that contains different values between participant and completion will be the answer.

result
1. in accuracy: quite alright
2. in efficiency: 
- it cannot be as space-efficient as I wish it were because two extra dicts have to be created.
- It will be actually quite inefficient space-wise

room for improvement
- come up with a solution that can be done without extra space required or at least less space.
"""


def first_try(participant, completion):
    p_dict = count_runners(participant)
    c_dict = count_runners(completion)

    return find_unfinished(p_dict.keys(), p_dict, c_dict)


def count_runners(runners):
    runner_counts = {}

    for runner in runners:
        if not runner_counts.get(runner):
            runner_counts[runner] = 1
        else:
            runner_counts[runner] = runner_counts.get(runner) + 1

    return runner_counts


def find_unfinished(p_dict_keys, p_dict: Dict[str, int], c_dict: Dict[str, int]):
    for key in p_dict_keys:
        if p_dict.get(key) != c_dict.get(key) or c_dict.get(key) is None:
            return key


"""
not a second try but a solution found on Programmers.

Counter objects are similar to dictionaries, but subject to subtraction.
Since only one runner is meant to fail the race, this way works with much more simplicity  
"""


def second_try(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

