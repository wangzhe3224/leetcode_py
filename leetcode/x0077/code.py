from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        # 方法1
        comb = [0 for _ in range(k)]
        def backtracking(comb, count, pos, n, k):
            
            if count >= k:
                res.append(comb[:])
                return 
                
            for i in range(pos, n+1):
                # 改变状态
                comb[count] = i
                count += 1
                # 继续搜索
                backtracking(comb, count, i+1, n, k)
                # 回滚状态
                count -= 1
            
        backtracking(comb, 0, 1, n, k)

        # 方法2
        def bt2(track: List[int], pos: int):
            if len(track) == k:
                res.append(track[:])
                return 
            
            for i in range(pos, n+1):
                track.append(i)
                bt2(track, i+1)
                track.pop(-1)
        track = []
        bt2(track, 1) 
        
        return res