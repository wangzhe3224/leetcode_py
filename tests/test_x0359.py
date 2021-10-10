import pytest

from leetcode.x0359.code import Logger

def test_logger():
    
    l = Logger()
    
    assert l.shouldPrintMessage(1, "foo") == True
    assert l.shouldPrintMessage(2, "bar") == True
    assert l.shouldPrintMessage(3, "foo") == False
    assert l.shouldPrintMessage(11, "foo") == True
    assert l.shouldPrintMessage(11, "foo") == True
    assert l.shouldPrintMessage(8, "bar") == False
    