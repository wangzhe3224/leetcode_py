# [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)

## 题目

给定一个 m × n 大小的非负整数矩阵，求从左上角开始到右下角结束的、经过的数字的和最 小的路径。
每次只能向右或者向下移动。

```text
Input:
 [[1,3,1],
  [1,5,1],
  [4,2,1]]
Output: 7
```

## 思路

求最值，大概率都是动态规划题，动态规划题首先找状态。我们有两个维度，行和列 `dp[i][j]`.

`dp[i][i] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]`

结果就是 `dp[m-1][n-1]`, mn 是 grid 的形状。
