# Leetcode in Python

项目组织结构如下：

```bash
- leetcode
  - x{leetcode题目编号}
    * readme.me <- 讲解思路，并给出原题链接
    * code.py   <- 代码
- tests （包含一些测试，但是目前非常不完整。。。）
```

- [Leetcode in Python](#leetcode-in-python)
  - [贪心算法](#贪心算法)
  - [Two pointer](#two-pointer)
  - [Binary Search](#binary-search)
  - [Sort](#sort)
  - [Search (DFS/BFS/...)](#search-dfsbfs)
  - [动态规划](#动态规划)
  - [工程相关](#工程相关)
    - [限流](#限流)

## 贪心算法

- [455. Assign Cookies](/leetcode/x0455/readme.md)
- [135. Candy](leetcode/x0135/readme.md)
- [435. Non-overlapping Intervals](leetcode/x0135/readme.md)
- [605. Can Place Flowers](leetcode/x0605/readme.md)
- [452. Minimum Number of Arrows to Burst Balloons](leetcode/x0452/readme.md)
- [763. Partition Labels](leetcode/x0763/readme.md)
- [122. Best Time to Buy and Sell Stock II](leetcode/x0122/readme.md)
- [406. Queue Reconstruction by Height](/leetcode/x0406/readme.md)

## Two pointer

- [1. Two Sum](/leetcode/x0001/readme.md)
- [3. Longest Substring Without Repeating Characters](leetcode/x0003/readme.md)
- [167. Two sum](leetcode/x0167/code/readme.md)
- [142. Linked List Cycle II](leetcode/x0142/readme.md)
- [76. Minimum Window Substring (Hard)](leetcode/x0076/readme.md)
- [633. Sum of Square Numbers](leetcode/x0633/readme.md)
- [524. Longest Word in Dictionary through Deleting](leetcode/x0524/readme.md)
- [88. Merge Sorted Array](leetcode/x0088/readme.md)

## Binary Search

- [69. Sqrt(x)](leetcode/x0069/readme.md)
- [34. Find First nd Last Position of Element in Sorted Array](/leetcode/x0034/readme.md)
- [81. Search in Rotated Sorted Array II](leetcode/x0081/readme.md)
- [154. Find Minimum in Rotated Sorted Array II](leetcode/x0154/readme.md)

## Sort

- [基本算法](leetcode/sort/readme.md)
- [215. Kth Largest Element in an Array](/leetcode/x0215/readme.md)
- [347. Top K Frequent Elements](/leetcode/x0347/readme.md)
- [451. Sort Characters By Frequency](/leetcode/x0451/readme.md)

## Search (DFS/BFS/...)

- DFS
  - [695. Max Area of Island](/leetcode/x0695/readme.md)
  - [547. Number of Provinces](/leetcode/x0547/readme.md)
  - [417. Pacific Atlantic Water Flow](/leetcode/x0417/readme.md)
- Backtrack
  - [46. Permutations](/leetcode/x0046/readme.md)
  - [77. Combinations](/leetcode/x0077/readme.md)
  - [79. Word Search](/leetcode/x0079/readme.md)
  - [51. N-Queens](/leetcode/x0051/readme.md)
- BFS
  - [934. Shortest Bridge](leetcode/x0934/readme.md)
  - [127. Word Ladder](leetcode/x0127/Readme.md)
- Binary Tree
  - [257. Binary Tree Path](leetcode/x0257/readme.md)

## 动态规划

动态规划问题和搜索问题有很多共同的地方
> 通俗一点来讲，动态规划和其它遍历算法(如深/广度优先搜索)都是将原问题拆成多个子问 题然后求解，他们之间最本质的区别是，动态规划保存子问题的解，避免重复计算。解决动态规 划问题的关键是找到状态转移方程，这样我们可以通过计算和储存子问题的解来求解最终问题。同时，我们也可以对动态规划进行空间压缩，起到节省空间消耗的效果。这一技巧笔者将在 之后的题目中介绍。

- 一维
  - [70. Climbing Stairs](leetcode/x0070/readme.md)
  - [198. House Robber](leetcode/x0198/readme.md)
  - [413. Arithmetic Slices](leetcode/x0413/readme.md)
- 二维
  - [64. Minimum Path Sum](leetcode/x0064/readme.md)
  - [542. 01 Matrix](leetcode/x0542/readme.md)

## 工程相关

### 限流

- [359. Logger Rate Limiter](leetcode/x0359/readme.md)
