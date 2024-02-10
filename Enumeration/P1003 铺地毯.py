'''
2024/1/27 22:58

保存所有地毯信息
判断目标点是不是在地毯内
倒着找，找到了就输出该地毯的编号
'''
num_carpet = int(input())

all_carpet_info = []

for i in range(num_carpet):
    lx, ly, l, h = map(int, input().split())
    all_carpet_info.append([lx, ly, l, h])

des_x, des_y = map(int, input().split())

up_carpet = -1 

for i in range(num_carpet-1, -1, -1):
    now_carpet_l = all_carpet_info[i][0] + all_carpet_info[i][2]
    now_carpet_h = all_carpet_info[i][1] + all_carpet_info[i][3]

    if all_carpet_info[i][0] <= des_x <= now_carpet_l and all_carpet_info[i][1] <= des_y <= now_carpet_h:
        up_carpet = i+1
        break

print(up_carpet)