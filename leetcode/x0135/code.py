class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        length = len(ratings)
        
        res = [1] * length
        
        for i in range(1, length):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
                
        for i in range(length-1, 0, -1):
            if ratings[i] < ratings[i-1]:
                res[i-1] = max(res[i-1], res[i] + 1)
                # res[i] = res[i] + 1
                
        return sum(res)
                
"""
1 3 2 2 1

1 1 1 1 1

1 2 1 1 1

1 2 1 2 1
"""