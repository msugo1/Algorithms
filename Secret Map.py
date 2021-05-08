import re
"""
https://programmers.co.kr/learn/courses/30/lessons/17681
"""

"""
first try

it looked quite intimidating at first with some complicated pictures but it turned out to make use of a OR bit operation.

logic
1. do the OR operation with each of the two elements from the given arrays on every index.
    - bin will make your life easier as it automatically turns provided numbers into a binary form.
    - NOTE with 'bin': it returns any values in a pattern of '0b(binary)' as a 'STRING'     
2. slice the '0b' part away and then turn 1 into '#', 2 into ' '(blank)
    - re.sub only replaces the given string with one condition, so another replacement has been substituted for (string).replace 
    
for the first time, I'm satisfied with the answer that I come up with, which is simple and yet does not lose its readability (not to mention very pythonic)
"""


def solution(n, arr1, arr2):
    return [re.sub(r"1", "#", (bin(arr1[idx] | arr2[idx])[2:].zfill(n)).replace("0", " ")) for idx in range(n)]

