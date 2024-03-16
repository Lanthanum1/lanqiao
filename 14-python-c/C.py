n = int(input())  # 输入一个整数n，表示列表的长度
A = list(map(int, input().split()))  # 输入n个整数，构成列表A
B = list(map(int, input().split()))  # 输入n个整数，构成列表B
C = list(map(int, input().split()))  # 输入n个整数，构成列表C
new_X = sorted([A[_] - B[_] - C[_] for _ in range(n)], reverse=True)  # 计算列表A[_] - B[_] - C[_]的值，并按降序排序，存储在new_X中
new_Y = sorted([B[_] - A[_] - C[_] for _ in range(n)], reverse=True)  # 计算列表B[_] - A[_] - C[_]的值，并按降序排序，存储在new_Y中
new_Z = sorted([C[_] - A[_] - B[_] for _ in range(n)], reverse=True)  # 计算列表C[_] - A[_] - B[_]的值，并按降序排序，存储在new_Z中
ans, res_X, res_Y, res_Z, sum_X, sum_Y, sum_Z = 0, 0, 0, 0, 0, 0, 0  # 初始化变量ans, res_X, res_Y, res_Z, sum_X, sum_Y, sum_Z为0

# 遍历列表中的元素
for i in range(n):
    sum_X += new_X[i]  # 将new_X中第i个元素加到sum_X中
    res_X = i + 1  # 更新res_X为i+1
    if sum_X > 0:  # 如果sum_X大于0
        ans = max(ans, res_X)  # 更新ans为ans和res_X中的较大值

    sum_Y += new_Y[i]  # 将new_Y中第i个元素加到sum_Y中
    res_Y = i + 1  # 更新res_Y为i+1
    if sum_Y > 0:  # 如果sum_Y大于0
        ans = max(ans, res_Y)  # 更新ans为ans和res_Y中的较大值

    sum_Z += new_Z[i]  # 将new_Z中第i个元素加到sum_Z中
    res_Z = i + 1  # 更新res_Z为i+1
    if sum_Z > 0:  # 如果sum_Z大于0
        ans = max(ans, res_Z)  # 更新ans为ans和res_Z中的较大值

    if sum_X <= 0 and sum_Y <= 0 and sum_Z <= 0:  # 如果sum_X、sum_Y和sum_Z都小于等于0
        break  # 跳出循环

print(ans if ans else -1)  # 输出ans，如果ans为0，则输出-1
