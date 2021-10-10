from typing import List

class Solution:
    # 状态转移方程：dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        dp = [0 for _ in range(n+1)]
        dp[1] = nums[0]
        
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        
        return dp[n]