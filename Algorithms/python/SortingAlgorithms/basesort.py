# -*- coding utf-8 -*-

"""
经典排序算法： 插入排序 冒泡排序 【从小到大】
"""

def insertion_sort(array):
    '''
    :param array: 待排序数组
    插入排序的逻辑： 选择一个元素与整个排序数组进行比较放到合适的位置
    :return: 排序后的数组
    '''

    for i in range(1, len(array)):
        # 待插入的牌
        tmp = array[i]
        j = i
        while j > 0 and tmp < array[j-1]:
            # 在排好序的牌中比较，如果小于则后移一位
            array[j] = array[j-1]
            j -= 1
        array[j] = tmp

    return array


# 冒泡排序
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


# 归并排序
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    arr_r = merge_sort(array[:mid])
    arr_l = merge_sort(array[mid:])
    return merge(arr_r, arr_l)


def merge(arr_r, arr_l):
    arr_merge = []
    i, j = 0, 0
    # 依次比较，将最小值放入新的数组
    while i < len(arr_r) and j < len(arr_l):
        if arr_r[i] <= arr_l[j]:
            arr_merge.append(arr_r[i])
            i += 1
        else:
            arr_merge.append(arr_l[j])
            j += 1
    # 将某个剩余的部分 合并到总的数组
    arr_merge += arr_r[i:]
    arr_merge += arr_l[j:]
    return arr_merge


array = [1, 4, 3, 2, 9, 7]
print(insertion_sort(array))
print(bubbleSort(array))
print(merge_sort(array))
