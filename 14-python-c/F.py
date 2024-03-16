from collections import *
from heapq import *
from itertools import *
from string import *
from math import *
from bisect import *

# 定义输入函数
ii = lambda: int(input())
si = lambda: input().split()
mi = lambda: map(int, si())
li = lambda: list(mi())

# 获取输入的 n 和 m
n, m = mi()

# 创建一个空列表 ops，用于存储操作
ops = [[] for _ in range(m)]

# 获取 m 组操作，并存储到 ops 列表中
for i in range(m):
    ops[i] = li()

# 创建一个 n+1 行 n+1 列的二维列表 chess，用于表示棋盘
chess = [[0] * (n+1) for _ in range(n+1)]

# 对每组操作进行处理
for i in range(m):
    x1, y1, x2, y2 = ops[i]
    chess[x1-1][y1-1] += 1
    chess[x2][y1-1] -= 1
    chess[x1-1][y2] -= 1
    chess[x2][y2] += 1

# 对棋盘进行前缀和计算
for i in range(1,n+1):
    chess[0][i] += chess[0][i-1]
    chess[i][0] += chess[i-1][0]

# 对棋盘进行二维前缀和计算
for i in range(1, n+1):
    for j in range(1, n+1):
        chess[i][j] += (chess[i-1][j] + chess[i][j-1] - chess[i-1][j-1])
        chess[i][j] %= 2

# 对棋盘的第一行和第一列进行取模运算
for i in range(n+1):
    chess[0][i] %= 2
    chess[i][0] %= 2

# 打印棋盘
for i in range(n):
    for j in range(n):
        print(chess[i][j], end="")
    print()
