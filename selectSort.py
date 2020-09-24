# -*- coding:utf-8 -*-
# Author:Candlia
'''
直接选择排序：从序列中选择关键字最小（大）的记录进行放置，直到整个序列所有记录选完为止。
第一次在N个记录选择最小的与第一位交换；
第二次在N-1记录中选择最小的与第二位交换；
在第i次在N-i+1的元素中选择最小的与第i位交换，直到整个序列有序为止
主要步骤：
1》令i=0
2》在无序序列中找到关键字值最小的记录Amin
3》Amin与Ai交换位置，i+1
4》重复步骤2,3，直到i=n-2
'''

def selectSort(arr):  #降序冒泡
    for i in range(len(arr)-1):
        tmp = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[tmp]:
                tmp = j
        arr[i], arr[tmp] = arr[tmp], arr[i]
    return arr


if __name__ == "__main__":
    testlist = [36, 23, 18, 56, 78, 70, 45, 2]
    print(selectSort(testlist))