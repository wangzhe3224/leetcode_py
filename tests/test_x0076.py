from leetcode.x0076.code import sol

def test():
    
    tests = {
        ( "ADOBECODEBANC", "ABC" ): "BANC",
        ( "aa", "a" ): "a",
        ( "a", "aa" ): "",
    }
    
    print(f"testing {sol.__module__}")

    for args, exp in tests.items():
        res = sol(*args)
        assert res == exp