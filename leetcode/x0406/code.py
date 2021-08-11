class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        # [[7, 0], [7, 1], [6, 1], [5,0], [5,2], [4,4]]
        # print(people)
        
        res = []
        
        for p in people:
            res.insert(p[1], p)
            
        return res
        
        