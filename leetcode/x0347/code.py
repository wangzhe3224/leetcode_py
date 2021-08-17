class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) <= k:
            return nums
        
        d = collections.defaultdict(int)
        for n in nums:
            d[n] += 1

        reverse = [(v, key) for key, v in d.items()]
        # count, num
        res = []   
        for n in sorted(reverse, reverse=True, key=lambda x: x[0])[:k]:
            res.append(n[1])
            
        return res