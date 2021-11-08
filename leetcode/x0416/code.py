class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # select subset that sums to sum(nums) / 2
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        
        target = _sum // 2
        n = len(nums)
        
        dp = [[False for _ in range(target+1)] for _ in range(n+1)]
        dp[0][0] = True
        
        for i in range(1, n+1):
            for j in range(target+1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                    
        return dp[n][target]