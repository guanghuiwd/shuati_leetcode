"""
森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。我们将这些回答放在 answers 数组里。
输入: answers = [1, 1, 2]
输出: 5

思路有但是算法没有这么精致的下沉，注意
"""
from collections import Counter

if __name__ == '__main__':
    from collections import Counter

    answers = [1, 1, 2, 3, ]
    count = 0
    answer_freq = Counter(answers)
    for answer, freq in answer_freq.items(): #标准的遍历了字典
        if freq % (answer + 1) == 0:
            count += freq  # 这类数量的颜色完全统计了
        else:
            count += (freq // (answer + 1) + 1) * (answer + 1)  # //取整除-返回商的整数部分（向下取整）
    print(count)
