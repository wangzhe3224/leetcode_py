
class Solution:
    def validPalindrome2(self, s: str) -> bool:
        i, j = 0, len(s)-1
        
        while i<j:
            if s[i] != s[j]:
                return self.check(s[i:j-1]) or self.check(s[i+1:j])
            else:
                i += 1
                j -= 1
                
        return True
                
    def check(self, s):
        return s == s[::-1]
    
    def validPalindrome(self, s: str):
        def verify(s, left, right, deleted):
            while left < right:
                if s[left] != s[right]:
                    if deleted:
                        return False
                    else:
                        return verify(s, left+1, right, True) or verify(s, left, right-1, True)
                else:
                    left += 1
                    right -= 1
            return True
        return verify(s, 0, len(s)-1, False)