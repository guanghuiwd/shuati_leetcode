"""
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。
"""
if __name__ == '__main__':
    people = [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]
    if not people:
        print([])
    people.sort(key=lambda x: x[1])  # 按面前几个高个子排序
    people.sort(key=lambda x: x[0], reverse=True)  # 按身高排序
    res = []
    for i in people:
        res.insert(i[1], i)  # 先插高的，后插矮的，即使后插的插到前面也不会有影响，因为矮。
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
