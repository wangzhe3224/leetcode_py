# [76. Minimum Window Substring (Hard)](https://leetcode.com/problems/minimum-window-substring/)

## 题解

这是一个滑动窗口问题，l..r 形成一个动态的窗口，求解最短的窗口。

```
 -------- -------
l--------r
   l-----r
   l---------r
       l-----r
       l---------r
            l----r
```

首先设置两个在0位置的指针：l 和 r。r开始右移，直到 l...r 包含了全部 t 中的字符，开始尝试缩短，将 l 向右移动，移动过程中检查目前l..r是否仍然满足条件（即包含t中所有字符）。然后判断当前 i..j 举例是否小于之前的最优解，如果小于就更新。最后进入r的下一次循环。

其中比较困难的是如何高效的判断当前 l...r 仍然包含全部t，一个可行的解法是：维护一个字典，他是t的counter，维护一个missing，就是l...r中还缺少的t中的字母数量。