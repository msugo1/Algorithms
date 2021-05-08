"""
https://programmers.co.kr/learn/courses/30/lessons/12901
"""

"""
first try

2016 - leap year, meaning that Feb sees 29 days

a - months
b - days

logic
- add all the days right until the target month followed by giving it (b-1) days
    : it is (b-1) because adding all the days before the target days puts you on the first of that month
- put Friday at first as Jan 1 2016 falls on Friday
- now divide the total days counts by 7
"""


def solution(a, b):
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    days_per_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days_counts = 0

    for mon in range(a - 1):
        days_counts += days_per_month[mon]

    days_counts += (b - 1)

    answer = days[days_counts % len(days)]
    return answer
