# [359. Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/)

## 题目

设计一个日志系统，接受一系列的信息，每条信息都有一个时间戳，日志系统
确保进当信息在过去的10秒内没有被打印的情况下打印该日志。

给出一个信息和时间戳（以秒计时），返回真如果满足打印条件，否则返回假。

可能很多信息具有相同的时间戳。

## 例子

```
Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;
```

## 思路

此题比较简单，只需要维护一个内部的字典即可：`msg-> last ts`.
