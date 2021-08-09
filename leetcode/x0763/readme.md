# [763. Partition Labels](https://leetcode.com/problems/partition-labels/)

## 题目

```text
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Input: s = "eccbbbbdec"
Output: [10]
```

## 思路

此题你看是求最多分成几个区，即求最值问题。可以考虑贪心算法。
或者此题也可以看成是区间问题，即找到相同字母形成的最长的没有重叠的区间。
要点在于首先用一个字典记录每一个字符的最后出现位置，然后维护双指针：
一个是i用来遍历，一个是mark，就是上一个没有重叠区间的边界索引。

```text
    ababcbacadefe
a   |-------|
b    |---|
c       |--|
d            |---
e             |-|   
```