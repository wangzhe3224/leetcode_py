# [413. Arithmetic Slices](https://leetcode.com/problems/arithmetic-slices/)

## 题目

## 思路

这道题首先第一步很自然想到，最短的情况是一个三个的等差数列，即
`nums[i] - nums[i-1] == nums[i-1] - nums[i-2]`。然后，
我们需要遍历数组。但是，复杂的地方在于，如果`[a,b,c]`是一个等差
数列，我们又发现`[b,c,d]`也是等差数列，我们马上得知`[a,b,c,d]`
也是！所以，在每一处i，我们记录当前位置最多的等差数列数量，这就是
我们的状态，状态转移方程为：`dp[i] = dp[i-1] + 1`。