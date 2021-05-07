import math
"""
https://programmers.co.kr/learn/courses/30/lessons/12977
"""
def solution(nums):
    ans = []

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                ans.append(nums[i] + nums[j] + nums[k])

    prime = []
    for num in ans:
        num_sqrt = math.sqrt(num)
        for divisor in range(2, int(num_sqrt) + 1):
            if num % divisor == 0:
                break
            if divisor == int(num_sqrt):
                prime.append(num)
    return prime


nums = [1, 2, 7, 6, 4]
print(solution(nums))