from leetcode.x0001.code import sol, sol_cache

def test_sol():
    
    params = [
        ([[1, 2], 3], [0, 1]),
        ([ [3,2,4], 6 ], [1, 2]),
    ]

    for args, exp in params:
        res = sol(*args)
        assert sorted(res) == sorted(exp)

    for args, exp in params:
        res = sol_cache(*args)
        assert sorted(res) == sorted(exp)