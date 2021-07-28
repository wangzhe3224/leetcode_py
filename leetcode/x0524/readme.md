# [524. Longest Word in Dictionary through Deleting](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/)

## 思路

此题有两个点：

1. 如何获得“有序”的字典列表
2. 如何判断一个str的字母是不是按照顺序包含在另一个str中

第一个点，我们排序有两个Key：长度和字符顺序，可以利用Python的 sort key

第二个点，利用双指针，逐个浏览字典中词，判断是不是sub str。sub str的判断通过遍历给出字符，然后按顺序判断是不是增加计数，最后计数与词长相同，则找到了解。