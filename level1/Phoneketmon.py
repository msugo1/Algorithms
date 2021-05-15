"""
logic
1. get the maximum number of phoneketmons to be able to have, which can take the number up, up to the half of the given list
: nums // 2
2. create an empty list that will contain phoneketmons with unique (or not repetitive) numbers
3. put the first one in a new list anyway because the given list should be bigger than 2 in size.
4. whilst in a for loop, put an element on the index if it is not already in the new list nor does the size exceed the limit.
5. return len(new list).

an O(n^2) solution - a nested 'in' operation with a list within a for loop

result
- some within 1ms but others take so much time as it is O(n^2)
- I was honestly surprised that it does not hit the time limit.
- a lot of rooms for improvement.
"""


def first_try(nums):
    max_val = len(nums) // 2
    phoneketmons = []

    for i in range(len(nums)):
        if i == 0:
            phoneketmons.append(nums[i])
        else:
            if len(phoneketmons) >= max_val:
                break
            else:
                if nums[i] not in phoneketmons:
                    phoneketmons.append(nums[i])

    answer = len(phoneketmons)
    return answer


num = [3, 1, 2, 3]
print(first_try(num))

# O(n)? solutions
"""
logic
- one type of a number can be picked out only once.
- the answer will be either everything gets picked out with still the size less than the limit
or the size gets over the limit with ease.
- whichever is smaller.
= 'min' comes to the stage here
 
- now the point is how to take out each element just one time.
= set
  

result 
- 20 tests each done within 1.00ms
what an astonishing improvement compared to the first try.
"""


def second_try(nums):
    answer = min(len(set(nums)), len(nums) // 2)
    return answer


print(second_try(num))


# the allocating a local variable process can be removed
def second_try_even_simpler(nums):
    return min(len(set(nums)), len(nums) // 2)
