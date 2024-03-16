from collections import *
from heapq import *
from itertools import *
from string import *
from math import *
from bisect import *

ii = lambda: int(input())  # 定义一个函数，用于读取整数输入
si = lambda: input().split()  # 定义一个函数，用于读取字符串输入并以空格分割
mi = lambda: map(int, si())  # 定义一个函数，用于将字符串输入转换为整数列表
li = lambda: list(mi())  # 定义一个函数，用于将字符串输入转换为整数列表

n = ii()  # 读取一个整数n，表示测试用例的数量
for _ in range(n):
    t = input()  # 读取一个字符串t
    s = input()  # 读取一个字符串s
    t = [x for x in t]  # 将字符串t转换为字符列表
    s = [x for x in s]  # 将字符串s转换为字符列表

    if s[0] != t[0] or s[-1] != t[-1]:  # 如果s的首字符不等于t的首字符或者s的尾字符不等于t的尾字符
        print("-1")  # 输出-1并继续下一个测试用例
        continue

    ans = 0  # 初始化答案为0
    for i in range(1, len(s) - 1):  # 遍历s中除去首尾字符的部分
        if s[i - 1] == s[i + 1] and s[i] != t[i] and s[i] != s[i - 1]:  # 如果s[i-1]等于s[i+1]且s[i]不等于t[i]且s[i]不等于s[i-1]
            ans += 1  # 答案加1
            s[i] = t[i]  # 将s[i]替换为t[i]

    if s != t:  # 如果s不等于t
        print("-1")  # 输出-1
        continue  # 继续下一个测试用例
    else:
        print(ans)  # 输出答案
