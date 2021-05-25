import collections

"""
    Q: https://programmers.co.kr/learn/courses/30/lessons/72411
    - it took literally days    
    
    Ideas
        1. get all the possible combinations in a list with recursion.
        2. count them with Counter dict
        3. get the max appearance for each combination that only appear more than 2 times.
        4. take out new menu strings with the same level of appearance as the max value.
        
    It was 'search with recursion' that holds the key, which I learned today from an answer to a similar question on Programmers.
    - make sure to revise or try to solve other questions with similar concepts. 
"""


def solution(given_strings, courses):
    def make_combinations_by_courses(str1, str2):
        if len(str1) in courses:
            combo.append(''.join(sorted(str1)))

        for idx in range(len(str2)):
            make_combinations_by_courses(str1 + str2[idx], str2[idx + 1:])

    def find_max_course_appearance(com: dict):
        for k, v in com.items():
            max_so_far = max_per_keys.get(len(k)) if len(k) in max_per_keys else v
            curr_max = max(v, max_so_far)
            if curr_max >= 2:
                max_per_keys[len(k)] = curr_max

    def select_new_menus(com: dict):
        for k, v in com.items():
            if max_per_keys.get(len(k)) == v:
                ans.add(k)

    combo = []

    for string in given_strings:
        make_combinations_by_courses("", string)

    max_per_keys = {}
    combinations = collections.Counter(combo)
    find_max_course_appearance(combinations)

    ans = set()
    select_new_menus(combinations)

    return sorted(ans)
