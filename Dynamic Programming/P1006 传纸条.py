'''
2024/2/11 00:46

第一版解法，这道题整了2个小时，整迷糊了。
结果这个答案还TLE

主要想说下
if i == x and j == y:
    continue
dp[i][j][x][y] = max(...)
这个是因为如果相同则不计算，
同时在输出时就不能输出dp[m][n][m][n]，因为不会计算，而是输出到dp[m][n-1][m-1][n]

如果改成
dp[i][j][x][y] = max(...)
if i == x and j == y:
    dp[i][j][x][y] -= s[i-1][j-1]
则最后需要输出dp[m][n][m][n]
'''
# m,n = map(int,input().split())
# s = []
# for i in range(m):
#     s.append(list(map(int,input().split())))
# dp = [[[[0 for j in range(n+1)]for i in range(m+1)]for y in range(n+1)]for x in range(m+1)]
# for i in range(1,m+1):
#     for j in range(1,n+1):
#         for x in range(1,m+1):
#             for y in range(1,n+1):
#                 if i == x and j == y:
#                     continue
#                 dp[i][j][x][y] = max(dp[i - 1][j][x - 1][y], dp[i][j - 1][x - 1][y], dp[i - 1][j][x][y - 1],dp[i][j - 1][x][y - 1]) + s[i-1][j-1] + s[x-1][y-1]
                  
# print(dp[m][n-1][m-1][n])

'''
2024/2/11 01:35
fuck you fuck you fuck you fuck you
fuck you
fuck you
fuck you

第二版解法：

多step去代替了位置，因为step可以根据所在的行来推出所在的列
也就是col_i, col_j = step - i + 1, step - j + 1

对于最后的输出：
dp[m+n-2][m][m]汇总了考虑所有规则（每步只能向右或向下，
每个位置的好心程度最多只能被一条路径收集一次）后，
通过所有可能路径到达终点(m, n)的最大好心程度之和。

对于循环中：
这一层循环遍历在给定步数step时，小渊可能到达的所有行位置i。
因为每一步小渊只能向右或向下移动，所以他在第step步时可能到达的最大行号是step（如果每步都向下移动）。
min(step+1, m)确保了不超出矩阵的行数m，同时考虑到了步数限制。
随着步数的增加，小渊可以到达的行号逐渐增多，但不会超过矩阵的最大行号m。

同理，如果是：
if i == j:
    continue
dp[step][i][j] = max(dp[step-1][i-1][j], 
                        dp[step-1][i][j], 
                        dp[step-1][i-1][j-1], 
                        dp[step-1][i][j-1])
dp[step][i][j] += s[i-1][col_i] + s[j-1][col_j]
则最后输出dp[m+n-3][m][m-1]或者dp[m+n-3][m-1][m]都一样

如果是
dp[step][i][j] = max(dp[step-1][i-1][j], 
                    dp[step-1][i][j], 
                    dp[step-1][i-1][j-1], 
                    dp[step-1][i][j-1]) + s[i-1][col_i] + (s[j-1][col_j] if i != j else 0)
则是输出dp[m+n-2][m][m]
'''
m,n = map(int,input().split())
s = []
for i in range(m):
    s.append(list(map(int,input().split())))

dp = [[[0 for _ in range(m+1)] for _ in range(m+1)] for _ in range(m+n-1)]


for step in range(1, m+n-1):
    for i in range(1, min(step+1, m)+1):
        for j in range(1, min(step+1, m)+1):
            col_i, col_j = step - i + 1, step - j + 1
            if col_i >= n or col_j >= n or col_i < 0 or col_j < 0: continue # 越界检查
            if i == j:
                continue
            dp[step][i][j] = max(dp[step-1][i-1][j], 
                                 dp[step-1][i][j], 
                                 dp[step-1][i-1][j-1], 
                                 dp[step-1][i][j-1]) + s[i-1][col_i] + s[j-1][col_j]


print(dp[m+n-3][m][m-1])