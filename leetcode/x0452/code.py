class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        [[1, 6], [2, 8], [7, 12], [10, 16]]
        [[1, 6], [2, 8], [7, 12], [10, 16]]
        ------
          --------
                 ------
                     -------
        """
        points = sorted(points, key = lambda x: x[1])
        res, end = 0, -float('inf')
        for interval in points:
            if interval[0] > end:
                res += 1
                end = interval[1]
        return res