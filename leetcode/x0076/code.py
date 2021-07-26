from collections import Counter

def sol(s: str, t: str) -> str:
    need = Counter(t)
    missing = len(t)
    start, end = 0, 0
    i = 0
    for j, char in enumerate(s, 1):  # j start from 1 ... len(s)-1
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        if missing == 0:  # found all chars in t in S
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            # 运行到这里，i移动到了第一个不满足的边界
            # 然后判断ij是否更短
            if end == 0 or j-i < end-start:
                start, end = i, j

            # 需要补齐missing和need
            need[s[i]] += 1
            missing += 1
            i += 1

    return s[start: end]
