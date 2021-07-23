# [167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## 题目

## 例子

## 思路

由于数组已经有序（从小达到）且保证有解，采用头尾双指针，向中间移动。如果发现和等于目标，返回；如果和小于目标，右移左指针；和大于目标，左移右指针。
