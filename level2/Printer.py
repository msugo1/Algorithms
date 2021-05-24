import collections

"""
    Q: https://programmers.co.kr/learn/courses/30/lessons/42587/solution_groups?language=python3&type=my
    
    Idea:
    - pop one from the left and check if it meets the requirement.
        1) put at the end if not the highest priority
        2) leave it out if it has the maximum value but not the target
            2 - 1) increment the count
        3) break the loop if the target with currently highest priority has been found.
         
    - need indices to keep track of the target's current situation
        (if it's max and ready to be printed)
    - deque is way more efficient here when it comes to popping left elements.
"""


def solution(priorities, location):
    pr_with_index = [(v, i) for i, v in enumerate(priorities)]
    deque = collections.deque(pr_with_index)

    pr_max = max(deque)[0]
    cnt = 1

    while deque:
        check = deque.popleft()

        if check[0] == pr_max and check[1] == location:
            break
        elif check[0] == pr_max:
            pr_max = max(deque)[0]
            cnt += 1
        else:
            deque.append(check)

    return cnt