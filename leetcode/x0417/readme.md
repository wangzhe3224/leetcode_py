# [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)

## 题目

```
Input:
太平洋 ~ ~ ~ ~ ~ 
    ~ 1 2 2 3 5 *
    ~ 3 2 3 4 4 *
    ~ 2 4 5 2 1 *
    ~ 6 7 1 4 5 *
    ~ 5 1 1 2 4 *
      * * * * * * 大西洋
Output: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
```

## 思路

这道题的关键在于转化成从海岸出发，逆向搜索，看每一个大洋可以走到哪里。然后遍历同时可以到达两个海洋的坐标。