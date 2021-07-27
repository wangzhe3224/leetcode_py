import math


def judgeSquareSum1(c: int) -> bool:
    nums = list(range(0, c+1))
    i, j = 0, c
    target = c
    # 0,1,2
    while (i<=j):
        
        _sum = nums[i]**2 + nums[j]**2
        
        if _sum == target:
            return True
        elif _sum < target:
            i += 1
        else:
            j -= 1
    
    return False

def judgeSquareSum(c: int):
    a = 0
    while a**2<=c:
        b = (c-a**2)**0.5
        if b == int(b):
            return True
        a += 1
    return False

def judgeSquareSum2(c: int):
    sq = set()
    count = int(math.sqrt(c))
    # use (count + 1) because first index is 0
    for i in range(count + 1):
        sq.add(i ** 2)

    for n in sq:
        if c - n in sq:
            return True

    return False