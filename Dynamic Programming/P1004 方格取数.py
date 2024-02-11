'''
2024/2/12 00:37
方法一，思路跟P1006很像
'''

# n = int(input())
# board = [[0 for j in range(n)]for i in range(n)]
# while 1:
#     x, y, num = (map(int,input().split()))
#     if x == y == num == 0:
#         break
#     board[x-1][y-1] = num

# dp = [[[[0 for j in range(n+1)]for i in range(n+1)]for y in range(n+1)]for x in range(n+1)]
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         for x in range(1,n+1):
#             for y in range(1,n+1):
                
#                 dp[i][j][x][y] = max(dp[i - 1][j][x - 1][y], dp[i][j - 1][x - 1][y], dp[i - 1][j][x][y - 1],dp[i][j - 1][x][y - 1]) + board[i-1][j-1] + board[x-1][y-1]
#                 if i == x and j == y:
#                     dp[i][j][x][y] -= board[i-1][j-1]

# print(dp[n][n][n][n])


'''
方法二，更快一些

注意，初始化dp[0][1][1] = s[0][0]，跟P1006有所不同，因为算上了初始位置的值。而在P1006中并没有
'''
n = int(input())
s = [[0 for j in range(n)]for i in range(n)]
while 1:
    x, y, num = (map(int,input().split()))
    if x == y == num == 0:
        break
    s[x-1][y-1] = num

dp = [[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+n-1)]

dp[0][1][1] = s[0][0]
for step in range(1, n+n-1):
    for i in range(1, min(step+1, n)+1):
        for j in range(1, min(step+1, n)+1):

            col_i, col_j = step - i + 1, step - j + 1
            if col_i >= n or col_j >= n or col_i < 0 or col_j < 0: continue # 越界检查

            dp[step][i][j] = max(dp[step-1][i-1][j], 
                                 dp[step-1][i][j], 
                                 dp[step-1][i-1][j-1], 
                                 dp[step-1][i][j-1]) + s[i-1][col_i] + s[j-1][col_j]
            if i == j:
                dp[step][i][j] -= s[i-1][col_i]
print(dp[n+n-2][n][n])