# [135. Candy](https://leetcode.com/problems/candy/)

## 题目

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

## 思路

首先每个小孩至少一个糖果，我们初始化一个全部为 1 的数组。首先从左向右遍历，比较左边和相邻的右边的rate，如果左边大于右边，则左边等于右边+1；
然后我们逆向遍历rate，如果左边大于右边，则左边等于max(左边，右边+1)。这里max是为了保证当前的左边保持让然比他的左边大（有第一次遍历决定的）