class Solution:
    def shortestBridge1(self, A: List[List[int]]) -> int:
        bound= set()
        dire = [(1,0),(-1,0),(0,1),(0,-1)]
        m, n = len(A), len(A[0])
        
        # get root of islanda
        def getfirst():
            for i in range(m):
                for j in range(n):
                    if A[i][j] == 1:
                        return i,j
        # get boundary of islanda
        def dfs(i,j):
            A[i][j] = -1
            for d in dire:
                x,y = i+d[0],j+d[1]
                if 0 <= x<m and 0 <= y < n:
                    if A[x][y] == 0:
                        bound.add((i,j))
                    elif A[x][y] == 1:
                        dfs(x,y)
        i,j = getfirst()
        dfs(i,j)
        # BFS to find next island
        step = 0
        while bound:
            new = []
            for i,j in bound:
                for d in dire:
                    x,y = i+d[0],j+d[1]
                    if 0 <= x < m and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif A[x][y] ==0:
                            A[x][y] = -1
                            new.append((x,y))
            step += 1
            bound = new
            
    def shortestBridge(self, A):
        n = len(A)
        # get one point from any island
        def getFirst():
            for i, row in enumerate(A):
                for j, point in enumerate(row):
                    if point == 1:
                        return (i,j)

        boundaries = set()
        # DFS first to find the boundary of first island
        stack = [getFirst()]
        while len(stack) > 0:
            i, j = stack.pop()
            # label it
            A[i][j] = -1
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n:
                    if A[x][y] == 0:
                        boundaries.add((i,j))
                    elif A[x][y] == 1:
                        stack.append((x,y))
        
        print(boundaries)
        
        # all the points on island A is stored in islandA now
        # BFS to expend it
        step = 0
        while boundaries:
            new = set()
            for i, j in boundaries:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            new.add((x, y))
            step += 1
            boundaries = new
            
    def sol(self, A):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n = len(A)
        for i, row in enumerate(A):
            for j, val in enumerate(row):
                if val == 1:
                    start = (i, j)
                    
        stack = [start]
        bound = []
        # find all island
        while stack:
            i, j = stack.pop()
            for dx, dy in directions:
                x, y = x+dx, y+dy
                if 0<=x<n and 0<=y<n:
                    if A[x][y] == 0:
                        bound.append((i, j))
                    elif A[x][y] == 1:
                        stack.append((x, y))
                        
        # explore boundaries
        step = 0
        while bound:
            newb = []
            for i, j in bound:
                for dx, dy in directions:
                    x, y = x+dx, y+dy
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            newb.append((x, y))
            step += 1
            bound = newb
            
    def shortestBridge2(self, grid: List[List[int]]) -> int:
        def paint(grid,i,j):
            if not 0<=i<len(grid) or not 0<=j<len(grid[0]):
                return 
            if grid[i][j]==1:
                grid[i][j] = 2
                paint(grid,i-1,j)
                paint(grid,i+1,j)
                paint(grid,i,j-1)
                paint(grid,i,j+1)
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    paint(grid,i,j)
                    break 
            else:
                continue 
            break 
        
        # print(grid)
        def expand(grid,i,j,n):
            if not 0<=i<len(grid) or not 0<=j<len(grid[0]):
                return   
            if grid[i][j]==0:
                grid[i][j] = n+1
            return grid[i][j]==1
        
        n = 2
        while True:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==n and (expand(grid,i-1,j,n) or expand(grid,i+1,j,n) or expand(grid,i,j+1,n) or\
                                          expand(grid,i,j-1,n)):
                        return n-2
            n += 1
    