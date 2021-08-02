class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r-l)//2
            if nums[m] > nums[r]:  # min in right
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r = r - 1
        return nums[l]
