# -*- coding utf-8 -*-


class HeapSort():

    def parent(self, i):
        return i//2

    def Left(self, i):
        return 2*i + 1 # 在实际使用中的index，下标从零开始的

    def Right(self, i):
        return 2 * i + 2

    def MaxHeapify(self, array, i):
        l = self.Left(i)
        r = self.Right(i)
        if l <= len(array) and array[l]>array[i]:
            largest = l
        else:
            largest = i
        if r <= len(array) and array[r]>array[largest]:
            largest = r
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            self.MaxHeapify(array, largest)

# python参数传递

heap_sort = HeapSort()
a = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
heap_sort.MaxHeapify(a, 1)
print(a)

