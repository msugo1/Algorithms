"""
Q.

Example

A.
"""

"""
first try

logic
- store distances in a dictionary like a graph
- if the next pressing button is in left or right only, append either
- if not, get the distance and compare, then add the shorter one to the answer string.

result
- it wouldn't pass the last 5 cases and I could not figure out why
- so I had to look up some hints to get some ideas on how to get to the point. 
"""


def solution(numbers, hand):
    answer = ''
    left_only = [1, 4, 7]
    right_only = [3, 6, 9]

    cur_left = '*'
    cur_right = '#'

    use_left_hand = 'L'
    use_right_hand = 'R'

    distances = {
        1: {2: 1, 5: 2, 8: 3, 0: 4}, 4: {2: 2, 5: 1, 8: 2, 0: 3},
        7: {2: 3, 5: 2, 8: 1, 0: 2}, '*': {2: 4, 5: 3, 8: 2, 0: 1},
        3: {2: 1, 5: 2, 8: 3, 0: 4}, 6: {2: 2, 5: 1, 8: 2, 0: 3},
        9: {2: 3, 5: 2, 8: 1, 0: 2}, '#': {2: 4, 5: 3, 8: 2, 0: 1},
        2: {2: 0, 5: 1, 8: 2, 0: 3}, 5: {2: 1, 5: 0, 8: 1, 0: 2},
        8: {2: 2, 5: 1, 8: 0, 0: 1}, 0: {2: 3, 5: 1, 8: 1, 0: 0}
    }

    for pressing_number in numbers:
        if pressing_number in left_only:
            cur_left = pressing_number
            answer += use_left_hand
            continue
        elif pressing_number in right_only:
            cur_right = pressing_number
            answer += use_right_hand
            continue
        else:
            distance_from_left = distances.get(cur_left).get(pressing_number)
            distance_from_right = distances.get(cur_right).get(pressing_number)

            if distance_from_left < distance_from_right:
                cur_left = pressing_number
                answer += use_left_hand
            elif distance_from_left == distance_from_right:
                if hand == 'right':
                    cur_right = pressing_number
                    answer += use_right_hand
                else:
                    cur_left = pressing_number
                    answer += use_left_hand
            else:
                cur_right = pressing_number
                answer += use_right_hand

    return answer


"""
second try

The hint described each dial location with x, y coordinate (x, y)

so,
    1(0, 0) 2(0, 1) 3(0, 2)
    4(1, 0) 5(1, 1) 6(1, 2)
    7(2, 0) 8(2, 1) 9(2, 2)
    *(3, 0) 0(3, 1) #(3, 2) 
"""


# I'll give it another go later
def solution_second_try(numbers, hand):
    location = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                "*": (3, 0), 0: (3, 1), "#": (3, 2)}

    left_only, right_only = [1, 4, 7], [3, 6, 9]
    use_left, use_right = "L", "R"
    left_curr, right_curr = "*", "#"
    res = ""

    for num in numbers:
        if num in left_only:
            res += use_left
            left_curr = num
        elif num in right_only:
            res += use_right
            right_curr = num
        else:
            destination, left_curr_pos, right_curr_pos = location[num], location[left_curr], location[right_curr]
            distance_from_left = abs(destination[0] - left_curr_pos[0]) + abs(destination[1] - left_curr_pos[1])
            distance_from_right = abs(destination[0] - right_curr_pos[0]) + abs(destination[1] - right_curr_pos[1])

            if distance_from_left > distance_from_right:
                res += use_right
                right_curr = num
            elif distance_from_left < distance_from_right:
                res += use_left
                left_curr = num
            else:
                if hand == "left":
                    res += use_left
                    left_curr = num
                else:
                    res += use_right
                    right_curr = num

    return res


nums = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
main_hand = "left"
print(solution_second_try(nums, main_hand))
