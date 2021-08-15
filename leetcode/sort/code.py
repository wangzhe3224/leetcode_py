import random

def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    p = random.choice(nums)

    left = quick_sort([x for x in nums if x < p])
    right = quick_sort([x for x in nums if x > p])

    return left + [x for x in nums if x == p] + right



if __name__ == "__main__":

    test = [1,3,2,4,2,6,4,8]
    # test = range(1, 1_000_000)
    print(quick_sort(test))
