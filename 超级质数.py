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

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 找到最大的超级质数

# 如果把超级质数看成一个字符串, 则这个超级质数的每个子串都是质数。

for k in range(99999999999999):
    flag = True
    s = str(k)
    if '1' in s or '4' in s or '6' in s or '8' in s or '9' in s:
        continue
    for i in range(len(s)):
        for j in range(i, len(s)):
            if not is_prime(int(s[i:j+1])):
                flag = False
    if flag:
        print(k)