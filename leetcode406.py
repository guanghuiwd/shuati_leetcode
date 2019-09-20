

if __name__ == '__main__':
    stature = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

    print("原始队列：")
    print(stature)

    # 按身高排列
    for i in range(0, len(stature) - 1):
        for i in range(0, len(stature) - 1):
            if stature[i][0] < stature[i + 1][0]:
                term = stature[i + 1]
                stature[i + 1] = stature[i]
                stature[i] = term
    print("按照身高排列的队列：")
    print(stature)

    output = []
    for item in stature:
        output.insert(item[1], item)

    print("最终队列：")
    print(output)
