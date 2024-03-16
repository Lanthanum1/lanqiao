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

s = input()
n = len(s)
# 因为是不重叠的，所以每次遍历连续的两个就可以
judge = ['00', '11', '0?', '1?', '?0', '?1', '??']
ans = 0
i = 1
while i < n:
    if s[i-1:i+1] in set(judge):
        ans += 1
        i += 2
    else:
        i += 1
print(ans)
