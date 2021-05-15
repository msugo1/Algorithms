"""
https://programmers.co.kr/learn/courses/30/lessons/64061
"""

"""
first try

logic
1. this crane has the height of the whole list size
    - it should go further down either till it hits the very bottom or a number that is not 0, equivalent to being not empty.
    - set the list size as maximum height
2. a list can also act as a stack in Python, so create an empty list instead
3. let a variable that will count numbers offset
4. along iterating the move elements, look up a valid number that's not 0 for each element from the height 0
5. when something not zero spotted, it should be dealt with in two ways: with and without an empty stack
- or it will pose an out of index error.
- don't forget to set the element 0
- then break the current loop for the next move
    1) with an empty stack - append
    2) if not empty, compare the last element.
        - remove the last element from the stack and increment the offset counts if they are the same 
        else just append the new element.
6. empty the element already removed or drawn to a stack by changing it to 0
7. then break the current loop
"""


def solution(board, moves):
    max_height = len(board)
    stack_dolls_storage = []
    answer = 0

    for move in moves:
        for height in range(max_height):
            width = move - 1
            current_doll = board[height][width]
            if current_doll != 0:
                if len(stack_dolls_storage) == 0:
                    stack_dolls_storage.append(current_doll)
                    board[height][width] = 0
                    break
                else:
                    last_doll = stack_dolls_storage[len(stack_dolls_storage) - 1]
                    if current_doll == last_doll:
                        stack_dolls_storage.pop()
                        answer += 2
                    else:
                        stack_dolls_storage.append(current_doll)
                    board[height][width] = 0
                    break

    return answer


"""
how can the code be improved to be more concise and elegant

1. let the stack contain 0 by default
- zero will never come in anyway. Secondly, it won't cause any out of index errors.
- I guess now it does not need any validity process to check whether it's an empty stack.

It is O(n^2) when it comes to time complexity
- can it be changed to be equivalent to or faster than O(n)?
"""


def try_second(board, moves):
    max_height = len(board)
    stack_dolls_storage = [0]
    answer = 0

    for move in moves:
        for height in range(max_height):
            current_doll = board[height][move - 1]
            if current_doll != 0:
                last_doll = stack_dolls_storage[len(stack_dolls_storage) - 1]
                if current_doll == last_doll:
                    stack_dolls_storage.pop()
                    answer += 2
                else:
                    stack_dolls_storage.append(current_doll)
                board[height][move - 1] = 0
                break

    return answer
