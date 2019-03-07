# -*- coding utf-8 -*-

"""
快速排序实现
"""


def quick_sort(array):
    # 分而治之 递归
    if len(array) >= 2: # 递归的入口与出口
        mid = array[len(array)//2]
        left, right = [], []
        array.remove(mid) # 移除基准值
        for num in array:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return array

# 非递归实现
# 一般情况下 递归转非递归就是用 栈来实现，因为递归实质也是用栈来实现的


if __name__ == '__main__':
    array = [1, 4, 10, 3, 2, 9, 7]
    print(quick_sort(array))