from typing import List

def sol(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    """ nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 """

    pos = m+n-1
    m -= 1
    n -= 1

    while (m>=0 and n>=0):
        if nums1[m] >= nums2[n]:
            nums1[pos] = nums1[m]
            m -= 1
        else:
            nums1[pos] = nums2[n]
            n -= 1
        pos -= 1

    while (n >= 0):
        nums1[pos] = nums2[n]
        n -= 1
        pos -= 1
