from collections import defaultdict

def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    
    left, right, res = 0, 0, 1
    flag = defaultdict(int)
    flag[s[left]] = 1
    
    while (left < len(s)):
        
        if right+1 < len(s) and flag.get(s[right+1], 0) == 0:
            flag[s[right+1]] += 1
            right += 1
        else:
            flag[s[left]] -= 1
            left += 1

        res = max(res, right-left+1)
        
    return res