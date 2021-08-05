class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[-1])
        print(intervals)
        
        remove = 0
        prev = intervals[0][-1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev:
                remove += 1
            else:
                prev = intervals[i][-1]
                
        return remove