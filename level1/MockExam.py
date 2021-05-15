"""
https://programmers.co.kr/learn/courses/30/lessons/42840
"""

"""
first try
"""


def solution_first(answers):
    first_student_pattern = [1, 2, 3, 4, 5]
    second_student_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    third_student_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    first_student_answers_count = 0
    second_student_answers_count = 0
    third_student_answers_count = 0

    for index in range(len(answers)):
        if first_student_pattern[index % len(first_student_pattern)] == answers[index]:
            first_student_answers_count += 1
        if second_student_pattern[index % len(second_student_pattern)] == answers[index]:
            second_student_answers_count += 1
        if third_student_pattern[index % len(third_student_pattern)] == answers[index]:
            third_student_answers_count += 1

    max_answers_count = max(first_student_answers_count, second_student_answers_count, third_student_answers_count)

    answer = []
    if first_student_answers_count == max_answers_count:
        answer.append(1)
    if second_student_answers_count == max_answers_count:
        answer.append(2)
    if third_student_answers_count == max_answers_count:
        answer.append(3)

    return answer


"""
second try
- rather than allocating separate answer counts, putting them all in one list and iterating through enumerate simplifies
the code a bit.
- both the first and second are not content speed-wise, but I cannot come up with an answer with better performance for now.
- maybe I'll have a go another time and see.
"""


def solution_second(answers):
    s1_pattern = [1, 2, 3, 4, 5]
    s2_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    s3_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer_counts = [0, 0, 0]

    for index in range(len(answers)):
        if s1_pattern[index % len(s1_pattern)] == answers[index]:
            answer_counts[0] += 1
        if s2_pattern[index % len(s2_pattern)] == answers[index]:
            answer_counts[1] += 1
        if s3_pattern[index % len(s3_pattern)] == answers[index]:
            answer_counts[2] += 1

    res = []
    for index, answers_count in enumerate(answer_counts):
        if max(answer_counts) == answers_count:
            res.append(index + 1)

    return res
