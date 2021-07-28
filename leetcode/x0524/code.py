class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        
        for w in dictionary:
            i = 0
            for c in s:
                if i < len(w) and w[i] == c:
                    i += 1
            
            if i == len(w):
                return w
            
        return ''
