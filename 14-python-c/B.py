ans = 0


def dfs(depth, n, m):
    global ans
    if depth == 7:
        if n == 0 and m == 0:  # 全部分完了，满足条件
            ans += 1
            return
    for i in range(0, n + 1):  # 第一种糖果
        for j in range(0, m + 1):  # 第二种糖果
            if i + j <= 5 and i + j >= 2 and i <= n and j <= m:
                dfs(depth + 1, n - i, m - j)  # 减掉当前分的情况，继续分下去


dfs(0, 9, 16)
print(ans)
