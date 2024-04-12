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
t = input()
s = [x for x in s]

cnt = 0
for i, c in enumerate(s[:-1]):
    if s[i] != t[i]:
        s[i+1] = '*' if s[i+1] == 'o' else 'o'
        cnt += 1
print(cnt)






        
        
