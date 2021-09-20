class Solution:
    def climbStairs1(self, n: int) -> int:
        dp = {}
        
        def helper(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            if n in dp:
                return dp[n]
            else:
                res = helper(n-1) + helper(n-2)
                dp[n] = res
                return res
            
        return helper(n)
    
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        state = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            state[i] = state[i-1] + state[i-2]
            
        return state[n]