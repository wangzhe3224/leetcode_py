# [406. Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/)

## 题目

## 思路

此题是个比较隐晦的贪心算法。基本的模式还是先排序，但是如何排确实很巧妙。
首先根据第一个元素降序，第一个元素相同，按照第二个元素升序。
然后，下一个巧妙的地方在于使用list的insert函数，将第二个元素作为index插入。