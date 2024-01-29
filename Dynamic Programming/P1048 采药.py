'''
2024/1/30 00:44

01背包问题
现在容量为w, 还可以拿k件物品

          | f(k-1, w), w^k > w (太重放不下) 
f(k,w) = -|
          | max( f(k-1, w), f(k-1, w - w^k) + v^k ), w^k <= w
'''     


import numpy as np

threshold_time, cla = map(int, input().split())

t = []  # 时间
v = []  # 价值

# 首个都是0
t.append(0)
v.append(0)
for i in range(cla):
    n_t , n_v = map(int, input().split())
    t.append(n_t)
    v.append(n_v)

# 同理创建表格
f = np.zeros(((cla+1), (threshold_time+1)))
for i in range(1, (cla+1)):
    for j in range(1, (threshold_time+1)):
        if(t[i] > j):
            f[i][j] = f[i-1][j]  # 如果比现在的门限大就取上一个
        else:
            f[i][j] = max(f[i-1][j], f[i-1][j-t[i]] + v[i])  # 如果小就需要比较不取和取谁的价值更大
# print(int(f[cla][threshold_time]))
print(f)
