class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        1 1 0
        1 1 0
        0 0 1
        """
        def dfs(conn, i, seen):
            seen[i] = True
            for k in range(len(conn)):
                if not seen[k] and conn[i][k]==1:
                    dfs(conn, k, seen)
                    
        count = 0
        
        seen = [False] * len(isConnected)
        for i in range(len(isConnected)):
            if not seen[i]:
                dfs(isConnected, i, seen)
                count += 1
                
        return count