'''
2024/2/8 21:32

dp[i][j]=max k<i (dp[k][j-1] * num[k+1:i])

dp[j][k-1]是在前j位数字中插入k-1个乘号所得到的最大乘积。
int(numStr[j:i])是从第j+1位到第i位数字组成的数的值。
max(dp[i][k], ...)确保dp[i][k]总是存储在前i位数字中插入k个乘号可以得到的最大乘积。
'''
n, K = map(int, input().split())
numStr = input()


# 初始化DP数组
dp = [[0] * (K+1) for _ in range(n+1)]
# 填充dp数组的第一列，没有乘号时的情况
for i in range(1, n+1):
    dp[i][0] = int(numStr[:i])  # 前i位数字组成的数

for i in range(1, n+1):
    for k in range(1, min(i, K+1)):  # i个数字最多插入i-1个乘号
        for j in range(1, i):
            # 更新dp[i][k]为所有可能分割方法中的最大乘积
            dp[i][k] = max(dp[i][k], dp[j][k-1] * int(numStr[j:i]))

print(dp[n][k])

