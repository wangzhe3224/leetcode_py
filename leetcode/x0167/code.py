from typing import List


def sol(nums: List[int], target: int) -> List[int]:
    """ diff from 1. Two Sum, nums is ordered. """
    l, r = 0, len(nums)-1
    while l < r:
        _sum = nums[l] + nums[r]
        if _sum == target:
            return [l, r]
        elif _sum < target:
            l += 1
        else: 
            r -= 1

    return []