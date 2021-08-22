class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if len(heights) == 0 or len(heights[0]) == 0:
            return []
        
        l, w = len(heights), len(heights[0])
        # reach_a, reach_p = [[False]*w]*l, [[False]*w]*l  # Here is a Pythonic Bug... try to change reach_a[0][0] and print them.....
        reach_a, reach_p = [[False for _ in range(w)] for _ in range(l)], [[False for _ in range(w)] for _ in range(l)]
        
        directions = (-1, 0, 1, 0, -1)
        
        def dfs(matrix, reach, r, c):
            if (reach[r][c]):
                return
            
            reach[r][c] = True
            x, y = 0, 0
            
            for i in range(4):
                x = r + directions[i]
                y = c + directions[i+1]

                if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and matrix[r][c] <= matrix[x][y]:
                    dfs(matrix, reach, x, y)
                    
        for i in range(l):
            dfs(heights, reach_p, i, 0)
            dfs(heights, reach_a, i, w-1)
            
        for j in range(w):
            dfs(heights, reach_p, 0, j)
            dfs(heights, reach_a, l-1, j)
            
        res = []
        for i in range(l):
            for j in range(w):
                if reach_a[i][j] and reach_p[i][j]:
                    res.append([i, j])
                    
        return res