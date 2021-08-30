class Solution:
    def solveNQueens(self, n: 'int') -> 'List[List[str]]':
        def backtrack(i):
            if i == n:
                res.append(list(board))
            for j in range(n):
                if j not in cols and j-i not in diag and j+i not in off_diag:
                    # 需要记录4个状态：答案，不可用的列、不可用的两个对角线
                    cols.add(j)
                    diag.add(j-i)
                    off_diag.add(j+i)
                    board.append("."*(j)+"Q"+"."*(n-j-1))
                    backtrack(i+1)
                    # 回滚四个装态
                    board.pop()
                    off_diag.remove(j+i)
                    diag.remove(j-i)
                    cols.remove(j)
        res = []
        board = []
        cols = set()
        diag = set()
        off_diag = set()
        backtrack(0)
        return res