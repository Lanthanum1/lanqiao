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
nums = li()
ht = set()
ht.add(0)
for x in nums:
    for y in list(ht):
        ht.add(x+y)
        ht.add(abs(x-y))
print(len(ht)-1)
