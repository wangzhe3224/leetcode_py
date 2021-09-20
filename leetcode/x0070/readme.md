# [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

## 题目

给定 n 节台阶，每次可以走一步或走两步，求一共有多少种方式可以走完这些台阶。

## 思路

走到第 i 阶的 方法数即为走到第 i-1 阶的方法数加上走到第 i-2 阶的方法数。这样我们就得到了状态转移方程 dp[i] = dp[i-1] + dp[i-2]。注意边界条件的处理。