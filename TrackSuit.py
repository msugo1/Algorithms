"""
Q.

Example

A.
"""

total_students = 5
students_lost_tracksuit = [2, 4]
reserved_tracksuit_size = [3]

"""
first try
1. messy
2. too much repetition
- urgent improvement is required
"""


def first_try(n, lost, reserve):
    students_currently_available = n - len(lost)

    if n == students_currently_available:
        return n

    students_rescued = []
    tracksuit_already_taken = []

    for student_number in lost:
        if student_number in reserve:
            students_rescued.append(student_number)
            tracksuit_already_taken.append(student_number)

        if students_currently_available + len(students_rescued) == n:
            return n

        lower_size = student_number - 1
        upper_size = student_number + 1

        if lower_size in reserve and lower_size not in tracksuit_already_taken:
            tracksuit_already_taken.append(lower_size)
            students_rescued.append(student_number)
            continue
        elif upper_size in reserve and upper_size not in tracksuit_already_taken:
            tracksuit_already_taken.append(upper_size)
            students_rescued.append(student_number)
            continue

    return students_currently_available + len(students_rescued)


# fail: 50% success


def second_try(n, lost, reserve):
    students_currently_available = n - len(lost)

    if n == students_currently_available:
        return n

    students_rescued = set()
    tracksuit_already_taken = []

    for student_number in lost:
        if student_number in reserve:
            students_rescued.add(student_number)
            tracksuit_already_taken.append(student_number)

    if students_currently_available + len(students_rescued) == n:
        return n

    for student_number in lost:
        lower_size = student_number - 1
        upper_size = student_number + 1
        if lower_size in reserve and lower_size not in tracksuit_already_taken:
            tracksuit_already_taken.append(lower_size)
            students_rescued.add(student_number)
            continue
        elif upper_size in reserve and upper_size not in tracksuit_already_taken:
            tracksuit_already_taken.append(upper_size)
            students_rescued.add(student_number)
            continue

    return students_currently_available + len(students_rescued)


# fail: 90% success
# I'll give it another go later
