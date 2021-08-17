class Solution:
    def frequencySort(self, s: str) -> str:
        freq = collections.defaultdict(int)
        
        for c in s:
            freq[c] += 1
            
        res = ''
        
        freq = sorted(freq.items(), key=lambda x: -x[-1])
        
        for c, q in freq:
            res += c*q
            
        return res