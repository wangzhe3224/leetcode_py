class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        
        while l <= r:  # <= is a conner case for [1] and 1
            mid = l + (r-l)//2
            
            if nums[mid] == target:
                return True
            elif nums[mid] <= nums[r]:
                # search right
                if target > nums[mid] and target <= nums[r]:
                    l += 1
                else:
                    r -= 1

            else:
                # search left
                if target < nums[mid] and target >= nums[l]:
                    r -= 1
                else:
                    l += 1
                    
        return False