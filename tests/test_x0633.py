from leetcode.x0633.code import *


def test_sol():
    
    params = [
        ([ 0 ], True),
        ([ 3 ], False),
    ]

    for args, exp in params:
        res = judgeSquareSum(*args)
        assert res == exp