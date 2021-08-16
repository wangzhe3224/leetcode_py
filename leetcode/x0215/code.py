class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        return nums[k-1]
    
    def findKthLargest(self, nums, k):
        if not nums:
            return 
        
        pivot = nums[-1]
        lower =  [x for x in nums if x > pivot]
        middle = [x for x in nums if x == pivot]
        upper =  [x for x in nums if x < pivot]
        
        L, M = len(lower), len(middle)
        
        if k <= L:
            return self.findKthLargest(lower, k)
        elif k > L + M:
            return self.findKthLargest(upper, k - L - M)
        else:
            return middle[0]
        
    def findKthLargest2(self, nums, k):
        if not nums: return
        
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]