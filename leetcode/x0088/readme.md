# [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

## 题目

## 例子

## 解答

nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

因为数组都有序，我们用m-1和n-1做两个指向两个数组最大值的指针，在添加一个pos指针用来跟踪当前位置。
对于m-1和n-1我们比较，把较大的一个放入pos位置，然后左移pos。如果循环结束后，
n-1指针比0大，我们就需要把num2中的元素复制到num1中；如果m-1比0大，我们不需要处理，因为nums1已经有序了。