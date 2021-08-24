class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []

        def bt(nums, track):
            # end condition
            if len(nums) == len(track):
                res.append(track[:])
                return

            for i in nums:
                if i in track:
                    continue

                # 修改节点状态
                track.append(i)
                # dfs
                bt(nums, track)
                # 回滚状态
                track.pop()

        bt(nums, track)
        return res
        