# O(n^2) 풀이법
def solution(nums):
    answer = 0
    max_val = len(nums) // 2
    pokemons = []

    for i in range(len(nums)):
        if i == 0:
            pokemons.append(nums[i])
        else:
            if len(pokemons) >= max_val:
                break
            else:
                if nums[i] not in pokemons:
                    pokemons.append(nums[i])

    answer = len(pokemons)
    return answer

num = [3,1,2,3]
print(solution(num))