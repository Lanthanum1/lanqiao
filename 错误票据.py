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
ans =[0] * 2
ht = set()
nums = []
for _ in range(n):
    nums1 = li()
    for x in nums1:
        nums.append(x)
        if x in ht:
            ans[1] = x
        ht.add(x)
nums.sort()
mn = nums[0]
for i in range(mn, 10 ** 5 + 1):
    if i not in ht:
        ans[0] = i
        break
print(ans[0], ans[1])
