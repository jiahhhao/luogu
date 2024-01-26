'''
2024/1/26 21:49

由于卒只能走右下，所以该点(x,y)只能是(x-1,y)或者(x,y-1)来的
所以可以地推出f(x,y) = f(x-1,y) + (x,y-1)
同时遇上马能到的地方设置为0，因为无法到达
改代码的时间复杂度为O(n^2)
'''

# import pprint  # 用于输出检验

n,m, cx,cy = map(int, input().split())

# 测试用例
# n,m,cx,cy = 6,6,3,3
# n,m,cx,cy = 8,4,4,2

# 马走的相对坐标
hx = [0,-2,-1, 1, 2, 2, 1, -1, -2]
hy = [0,1 , 2, 2, 1,-1,-2, -2, -1]


# 创建整个棋盘
buf_checkerboard = [[False] * (n+1) for _ in range(m+1)]


# 设置马能到的地方
for i in range(9):
    tmpx = cx+hx[i]
    tmpy = cy+hy[i]
    #  如果满足在棋盘内
    if 0 <= tmpx <= n and 0 <= tmpy <= m:
        buf_checkerboard[cy+hy[i]][cx+hx[i]] = True


# 初始位置是1
buf_checkerboard[0][0] = 1


for y in range(m+1):
    for x in range(n+1):
        #  如果是没遍历的就遍历
        if buf_checkerboard[y][x] == False:
            if (x):  # 判断是否为边界
                if repr(buf_checkerboard[y][x-1]) != 'True':  # 如果不是马占的地方
                    buf_checkerboard[y][x] += buf_checkerboard[y][x-1]
                else:
                    buf_checkerboard[y][x] += 0  # 是马占的就加0
            if (y):  # 判断是否为边界
                if repr(buf_checkerboard[y-1][x]) != 'True':
                    buf_checkerboard[y][x] += buf_checkerboard[y-1][x]
                else:
                    buf_checkerboard[y][x] += 0


# pprint.pprint(buf_checkerboard)
print(buf_checkerboard[m][n])