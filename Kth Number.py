"""
Q. get 'k'th number from an array that needs slicing from 'i'th to 'j'th followed by being sorted.

example
- arr = [1, 5, 2, 6, 3, 7, 4]
- com = [[2, 5, 3],  [4, 4, 1], [1, 7, 3]]

A: [5, 6, 3]
"""

"""
first try

logic
: assumed that duplicate elements lie in the given list, commands

1. look up the cache (dictionary here)
    1) exist
    - append the cached value
    2) not exist
        (1) get a sub list from i to j - can be done by list slicing in Python effortlessly
        NOTE: arrays or lists start from 0
        (2) sort the sublist - sorted or sort is known for its simplicity, as well as effectiveness with tim sort
        (3) get an element on the kth 
        (4) put the value not just in the answer list but also the cache for the later use.
"""


def solution(array: list, commands: list):
    answer = []
    cache = {}

    for command in commands:
        # command needs to be converted into a tuple that is immutable because keys for a hash table MUST BE immutable
        # , which means lists can be taken as keys with its mutability.
        # I did not realise it till I faced the issue and googled it.
        cached_target = cache.get(tuple(command))

        if cached_target:
            answer.append(cached_target)
        else:
            i, j, k = command
            sub_list = sorted(array[i - 1: j])
            target = sub_list[k - 1]
            answer.append(target)
            cache[tuple(command)] = target
    return answer
