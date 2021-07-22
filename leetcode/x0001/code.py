from typing import List


def sol(nums: List[int], target: int) -> List[int]:
    """ brute force.
    nums = [2, 7, 9, 1], target = 9
    res = [0, 1]
    """
    for i in range(len(nums)):
        a = nums[i]
        for j in range(i+1, len(nums)):
            b = nums[j]
            if a + b == target:
                return [i, j]

def sol_cache(nums: List[int], target: int) -> List[int]:
    """ fact: cache the distance of each number to target,
    if find a number who's distance is cached, return cahed number and current num
    """
    cache = {}

    for i in range(len(nums)):
        residual = target - nums[i] 

        if residual in cache:
            return [i, cache[residual]]
        else:
            cache[nums[i]] = i