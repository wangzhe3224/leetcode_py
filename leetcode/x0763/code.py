class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {}
        for idx, c in enumerate(S):
            last[c] = idx
        res = []
        j = mark = 0
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                res.append(i - mark + 1)
                mark = i + 1
                
        return res