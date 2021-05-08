"""
https://programmers.co.kr/learn/courses/30/lessons/42862
"""

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

"""
second try
"""


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

"""
third try - finally passed

basic logic
1. create a taken list
2. add any students that lose and bring an extra tracksuit - they can't lend them to anyone for their own good.
(1 - 2 can be combined into one with list comprehension)
3. now time to iterate in a for loop to find candidate tracksuits that are one size smaller or larger.
    1) skip one's that has the same number (already added above)
    2) add a smaller or bigger one for each student if the tracksuit is not taken yet.

* this logic assumes that one student may take two tracksuits such as lost = [2, 4, 5] / reserve = [1, 3, 5]
- However, student numbers are not duplicate, and already taken ones are not supposed to be given again.
- So, an assumption has been made that any one more tracksuit that's taken by a student can be offset 
  : by choosing whichever is smaller, the entire students or the number of students that are already available added to whoever managed to borrow tracksuits.   
  
I guess when lost = [2, 5] and reserve [1, 3], the answer should be 4 as it is only number 2 who can borrow JUST ONE tracksuit
- but the code below is meant to yield 5 as an answer.

* HOW COULD IT EVEN PASS ALL THE CASES?
- technically, it is accepted but I don't think it is solved with completion.
- it definitely needs refinement.

* the problem above has been solved at least for now by counting the students who have successfully come by extra tracksuits.
"""


def solution(n, lost, reserve):
    available = n - len(lost)

    taken = [student for student in lost if student in reserve]
    rescued = []

    for student in lost:
        if student in taken:
            continue

        if student not in rescued and student - 1 in reserve and student - 1 not in taken:
            taken.append(student - 1)
            rescued.append(student)

        if student not in rescued and student + 1 in reserve and student + 1 not in taken:
            taken.append(student + 1)
            rescued.append(student)

    return min(n, len(taken) + available)


total_students = 5
students_lost_tracksuit = [2, 5]
reserved_tracksuit_size = [1, 3]
print(solution(total_students, students_lost_tracksuit, reserved_tracksuit_size))
