# [934. Shortest Bridge](https://leetcode.com/problems/shortest-bridge/)

## 题目

## 思路

因此此题是求最短距离，需要广度搜索。
首先，我们需要用dfs找到第一座岛屿的范围，与此同时，记录第一座岛屿的边界。
然后，我们从边界出发，开始广度有限搜索，就是逐步扩大岛屿的圈，直到我们碰到另一个岛屿。
