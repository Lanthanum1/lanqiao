# 导入常用的Python库
from collections import *
from heapq import *
from itertools import *
from string import *
from math import *
from bisect import *

# 定义输入函数，用于简化输入操作
ii = lambda: int(input())  # 读取一个整数
si = lambda: input().split()  # 读取一行并分割成字符串列表
mi = lambda: map(int, si())  # 读取一行并转换为整数列表
li = lambda: list(mi())  # 将整数列表转换为列表

# 定义Trie节点类，用于构建Trie树
class TrieNode:
    def __init__(self):
        self.children = [None, None]  # 初始化两个子节点

    # 插入函数，用于将数字插入Trie树
    def insert(self, num: int):
        node = self
        for i in range(b_length, -1, -1):  # 遍历每一位二进制位
            bit = (num >> i) & 1  # 获取当前位的值
            if not node.children[bit]:  # 如果当前位的子节点不存在
                node.children[bit] = TrieNode()  # 创建新的Trie节点
            node = node.children[bit]  # 移动到下一个节点

    # 查询最大值函数，用于查询以当前节点为前缀的最大数
    def query_max(self, num: int) -> int:
        node = self
        res = 0
        for i in range(b_length, -1, -1):
            bit = (num >> i) & 1
            if node.children[1 - bit]:  # 如果当前位的反码子节点存在
                res += (1 << i)  # 累加到结果中
                node = node.children[1 - bit]  # 移动到反码子节点
            else:
                node = node.children[bit]  # 否则移动到当前位子节点
        return res

    # 查询最小值函数，用于查询以当前节点为前缀的最小数
    def query_min(self, num: int) -> int:
        node = self
        res = 0
        for i in range(b_length, -1, -1):
            bit = (num >> i) & 1
            if node.children[bit]:  # 如果当前位的子节点存在
                node = node.children[bit]  # 移动到当前位子节点
            else:
                res += (1 << i)  # 累加到结果中
                node = node.children[1 - bit]  # 移动到反码子节点
        return res

# 初始化全局变量
n = ii()  # 读取测试用例的数量
a = li()  # 读取每个测试用例的整数序列
b_length = max(a).bit_length() + 1  # 计算二进制表示的最大长度

lmax = [0] * (n + 2)
lmin = [inf] * (n + 2)
rmax = [0] * (n + 2)
rmin = [inf] * (n + 2)

# 初始化Trie树和辅助数组
ltrie = TrieNode()  # 创建左Trie树的根节点
ltrie.insert(0)  # 插入0作为前缀
ls = [0] * (n + 1)  # 初始化左前缀异或和数组

# 构建左Trie树并计算左右最大/最小值
for i in range(1, n + 1):
    ls[i] = ls[i - 1] ^ a[i - 1]  # 计算左前缀异或和
    lmax[i] = max(lmax[i - 1], ltrie.query_max(ls[i]))  # 更新左最大值
    lmin[i] = min(lmin[i - 1], ltrie.query_min(ls[i]))  # 更新左最小值
    ltrie.insert(ls[i])  # 插入左前缀异或和到左Trie树

# 初始化右Trie树和辅助数组
rtrie = TrieNode()  # 创建右Trie树的根节点
rtrie.insert(0)  # 插入0作为前缀
rs = [0] * (n + 2)  # 初始化右前缀异或和数组

# 构建右Trie树并计算左右最大/最小值
for i in range(n, 0, -1):
    rs[i] = rs[i + 1] ^ a[i - 1]  # 计算右前缀异或和
    rmax[i] = max(rmax[i + 1], rtrie.query_max(rs[i]))  # 更新右最大值
    rmin[i] = min(rmin[i + 1], rtrie.query_min(rs[i]))  # 更新右最小值
    rtrie.insert(rs[i])  # 插入右前缀异或和到右Trie树

# 计算最终结果
ans = 0
for i in range(1, n):  # 遍历所有整数
    ans = max(ans, max(lmax[i] - rmin[i + 1], rmax[i + 1] - lmin[i]))  # 更新最大差值

# 输出结果
print(ans)