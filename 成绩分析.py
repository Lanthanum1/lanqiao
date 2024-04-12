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

n = ii()
nums = [0] * n
for i in range(n):
    nums[i] = ii()
    
print(max(nums))
print(min(nums))
print(f"{sum(nums)/n:.2f}")
# 如果使用round，可能不足两位