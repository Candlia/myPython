# -*- coding:utf-8 -*-
# Author:Candlia
# for i in range(high-1, low-1, -1):
#     if list1[i] > p:
#         list1[low], list1[i] = list1[i], list1[low]
#         low += 1
#         break
# for i in range(low,high):
#     if list1[i] < p:
#         list1[high], list1[i] = list1[i], list1[high]
#         high -= 1
#         break
# list1[low] = p
# return low
'''
快速排序：分区交换排序算法，冒泡排序的改进，采用分治策略，|
将问题分成若干个规模更小但和原问题相似的子问题，
然后用递归算法解决这些子问题，最终将他们组合成原问题的解
时间复杂度：O（N log2N),最坏情况为待排序序列基本有序，每次只能划分出一个子序列，
等同于冒泡排序，
时间复杂度O（N*N）
空间复杂度：最坏O（N），其他O（log2N）
当基准N选取不合适时，快速排序较慢
步骤：
1》设置两个变量low，high，分别代表待排序序列的起始下标和终止下标
2》设置变量 P = list[low]
3》从下标为high的位置从后往前搜索，当找到第一个比P关键字值小的记录，
将该数据移动到下标为low的位置 ，low+1
4》从下标为low的位置从前往后搜索，当遇到第一个比P关键字大的记录，
将该数据移动到下标为high的位置，high-1
5》重复步骤3,4，直到low==high为止
6》list[low] = p
'''
def quikSort(list1, low, high):
    if low<high:
        p = Partition(list1, low, high)
        quikSort(list1, low, p - 1)
        quikSort(list1, p + 1, high)

def Partition(list1, low, high):
    p = list1[low]
    while low < high:
        while low < high and list1[high] >= p:
            high -= 1
        list1[low] = list1[high]
        while low < high and list1[low] <= p:
            low += 1
        list1[high] = list1[low]
    list1[low] = p
    print(list1)
    return low

if __name__ == '__main__':
    liat  = [45,53,24,18,36,72,30,48,93,15,36]
    quikSort(liat, 0, len(liat)-1)
    print(liat)