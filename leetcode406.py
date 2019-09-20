#

#先插高的，后插矮的，即使后插的插到前面也不会有影响，因为矮。

if __name__ == '__main__':
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

    people.sort(key=lambda x: [-x[0], x[1]])
    res = []
    for p in people:
        res.insert(p[1], p)
    print(res)




# 有问题的代码16/37 ac
# if __name__ == '__main__':
#     stature = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

#     print("原始队列：")
#     print(stature)

#     # 按身高排列
#     for i in range(0, len(stature) - 1):
#         for i in range(0, len(stature) - 1):
#             if stature[i][0] < stature[i + 1][0]:
#                 term = stature[i + 1]
#                 stature[i + 1] = stature[i]
#                 stature[i] = term
#     print("按照身高排列的队列：")
#     print(stature)

#     output = []
#     for item in stature:
#         output.insert(item[1], item)

#     print("最终队列：")
#     print(output)
