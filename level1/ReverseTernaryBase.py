"""
https://programmers.co.kr/learn/courses/30/lessons/68935
"""
"""
first try

logic
- recursion seems to be able to produce an promising solution when it comes to converting decimal numbers 
into numbers with other bases (here 3 - Injecting any required bases from outside could make it more flexible)
- anyways, the converted number that's string (into ternary base) does not have to be reversed again
because iterating from the first index is supposed to bring about the same result as the reversed one from the last index.   

In short,
1. convert the given number into the required base as a string form
2. iterate from the first letter and then sum each result that is the calculation of value on the index multiplied by 3^(idx) 
"""


def first_solution(n):
    ternary = convert_to_ternary_number(n)
    decimal = 0

    for idx, each_num in enumerate(ternary):
        decimal += (int(each_num) * pow(3, idx))

    return decimal


def convert_to_ternary_number(num):
    if num == 1:
        return str(num)

    base = num // 3
    remainder = num % 3

    return convert_to_ternary_number(base) + str(remainder)


# result  - 40% out of 100%. failed by runtime error
# range: 1 <= n <= 100,000,000 so, recursion causes RecursionError here
# another way other than recursion needs to be found

# print(first_solution(100000000))

"""
second try
- note the fact that recursion and iteration are mostly interchangable
"""


def second_solution(n):
    ternary = ''

    while n >= 1:
        base = n // 3
        remainder = n % 3
        ternary = str(remainder) + ternary
        n = base

    decimal = 0

    for idx, each_num in enumerate(ternary):
        decimal += (int(each_num) * pow(3, idx))

    return decimal


"""
another solution
- when turning a string to an integer, the level of base can be given as another argument.
- the result will be automatically transformed into decimal numbers.
"""


def third_solution(n):
    ternary = ''

    while n >= 1:
        base = n // 3
        remainder = n % 3
        ternary = ternary + str(remainder)
        n = base

    return int(ternary, 3)


def solution(numbers):
    answer = set()

    for i, i_val in enumerate(numbers):
        for j, j_val in enumerate(numbers):
            if i != j:
                two_sum = i_val + j_val
                answer.add(two_sum)

    return list(answer)


print(solution([5, 0, 2, 7]))
