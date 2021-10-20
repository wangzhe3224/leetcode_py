class Solution:

    def updateMatrix1(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        if not m:
            return None
        n = len(mat[0])
        f = [[float("inf") for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    f[i][j] = 0
                    continue
                if i > 0:
                    f[i][j] = min(f[i][j], f[i - 1][j] + 1)
                if j > 0:
                    f[i][j] = min(f[i][j], f[i][j - 1] + 1)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 0:
                    continue
                if i < m - 1:
                    f[i][j] = min(f[i][j], f[i + 1][j] + 1)
                if j < n - 1:
                    f[i][j] = min(f[i][j], f[i][j + 1] + 1)
        
        return f
    
    def updateMatrix(self, mat):
        
        row, col = len(mat), len(mat[0])
        dist = [[float("inf") for _ in range(row)] for _ in range(col)]
        
        queue = []
        
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))
                    
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        while queue:
            cr, cc = queue.pop(0)
            for i in range(4):
                nr, nc = cr+directions[i][0], cc+directions[i][1]
                if nr >= 0 and nc >=0 and nr < row and nc < col:
                    if dist[nr][nc] > dist[cr][cc]+1:
                        dist[nr][nc] = dist[cr][cc]+1
                        queue.append((nr, nc))
        
        return dist