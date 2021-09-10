# [127. Word Ladder](https://leetcode.com/problems/word-ladder/)

## 题目

## 思路

此题利用一个queue作为搜索结构容器，包含的状态是当前词和到这个词的长度。在循环过程中穷举所有可能的变一个字母的情况，把符
符合条件的字符放入queue中进一步搜索。