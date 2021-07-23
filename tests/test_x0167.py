from leetcode.x0167.code import sol

def test_sol():
    
    params = [
        ([ [1, 2], 3 ], [0, 1]),
        ([ [2,3,4], 6 ], [0, 2]),
    ]

    for args, exp in params:
        res = sol(*args)
        assert sorted(res) == sorted(exp)