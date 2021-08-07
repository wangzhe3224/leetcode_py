# [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

## 题目

```text
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
```

## 思路

此题的关键在于找到最多的重叠区域，因为这些重叠的区域就可以用一支箭搞定。怎么找呢？其实方法跟[435](../x0435/readme.md)非常类似：首先把区间按照最后一个数值排序，然后遍历所有区间。期间，维持两个临时变量：一个射箭数量，一个是上一个区间的结尾值。如果发现当前区间的第一个值大于上一个区间的结束值，累加射箭数量，并且更新上一个区间的结束值为当前区间的结束。

画出图形更容易理解整个流程。

```text
[[1, 6], [2, 8], [7, 12], [10, 16]]
------
  -------
        ------
            -------
```

所以，这类区间问题的关键是：首先排序，然后按照需求更新临时变量。