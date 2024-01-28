'''
2024/1/29 00:40
卡特兰数
下面提供一个学习链接：
https://zhuanlan.zhihu.com/p/97619085
'''
n = int(input())


#方法一：

ans = 1
for i in range(2, n + 1):
    ans = ans * (4 * i - 2) // (i + 1)
print(ans)


# 方法二： 导入库

# import math

# print(int(math.comb(2*n,n)/(n+1)))