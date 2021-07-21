import pytest

from leetcode.x0003.code import lengthOfLongestSubstring

def test():
    
    tests = {
        (" ", ): 1,
        ("", ): 0,
        ("aaa", ): 1,
        ( "abab",  ): 2,
        ( "ababbac",  ): 3,
    }
    
    print(f"testing {lengthOfLongestSubstring.__module__}")

    for args, exp in tests.items():
        res = lengthOfLongestSubstring(*args)
        assert res == exp