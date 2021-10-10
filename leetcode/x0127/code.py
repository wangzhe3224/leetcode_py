import collections
import string

class Solution(object):
    def sol(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        q = collections.deque((beginWord, 1))
        while q:
            w, l = q.popleft()
            if w == endWord:
                return l
            
            for i in range(len(w)):
                for c in string.ascii_lowercase:
                    next_w = w[:i] + c + w[i+1:]
                    if next_w in wordList:
                        wordList.remove(next_w)
                        q.append((next_w, l+1))
        
        return 0