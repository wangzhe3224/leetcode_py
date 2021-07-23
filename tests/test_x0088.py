from leetcode.x0088.code import sol

def test_sol():
    
    params = [
        ([ [1, 2, 3, 0, 0, 0], 3, [4,5,6], 3 ], [1,2,3,4,5,6]),
    ]

    for args, exp in params:
        nums1, _, _, _ = args
        sol(*args)
        assert sorted(nums1) == sorted(exp)