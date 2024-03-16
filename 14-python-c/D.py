import sys
import os
from collections import *
from heapq import *
from itertools import *
from string import *
from math import *
from bisect import *
ii = lambda: int(input())
si = lambda: input().split()
mi = lambda: map(int, si())
li = lambda: list(mi())

n = int(input())

# 每个数ai都是区间[0，9]的整数，所以创建列表，里面存放0-10中每个数字是第几个数
numbers = [[] for _ in range(10)]

# 长度为n的数组输入
for i in range(n):
    a, b = mi()
    numbers[a].append(b)  # 例如数字1，是第1,2,3个

ans = 0  # 代价为0
k = n//10  # 长度为n，有n//10个10
for i in range(10):
    # 对numbers[i]中的数进行从小到大排序，因为不用替换的数为最大的数
    # 例如：1，是第1，2，3，不用替换的数为3，即最大的数3
    ls = sorted(numbers[i])
# 代价和为-k前面的数的和
    ans += sum(ls[:-k])
print(ans)

# 举例，例如总共有20个数，1出现了5次，那么代价最大的那两个就不用替换；如果总共有30个数，1出现了5次，那么代价最大的那三个就不用替换
