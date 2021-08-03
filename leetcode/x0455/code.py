class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        gid, sid = 0, 0
        
        while (gid < len(g) and sid < len(s)):
            
            if g[gid] <= s[sid]:
                gid += 1
                
            sid += 1
                
        return gid