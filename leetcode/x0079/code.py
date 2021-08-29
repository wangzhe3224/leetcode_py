class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        self.res = False
        
        def dfs(i, j, pos):
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return
            
            if (i,j) in seen or self.res or board[i][j] != word[pos]:
                return 
            
            if pos == len(word)-1:
                self.res = True
                return
            
            # 改变状态
            seen.add((i, j))
            # 搜索
            dfs(i-1, j, pos+1)
            dfs(i+1, j, pos+1)
            dfs(i, j-1, pos+1)
            dfs(i, j+1, pos+1)
            # 回滚状态
            seen.remove((i, j))
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, 0)
        
        return self.res