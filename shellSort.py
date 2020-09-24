# -*- coding:utf-8 -*-
# Author:Candlia
'''
希尔排序：又称缩小增量排序，是对直接插入排序的改进算法。分组的直接插入排序，算法描述：
1、将一个数据元素序列分组，每组由若干个相隔一段距离的元素组成，
在一个组内采用直接插入算法进行排序
2、增量的初值通常为数据元素序列的一半，以后每趟增量减半，最后值为1.
随着增量逐渐减少，组数也减少，组内元素的个数增加，数据元素序列接近有序。
主要步骤：
1》设定一个增量序列
2》根据当前增量Di将间隔为Di的数据元素组成一个子表，共Di个子表
3》对各子表的数据元素进行直接插入排序
4》重复2,3，直到Di=1，此时序列已排好序
'''

def shellSort(mylist):
    d = len(mylist)//2 + 1
    while d > 1:
        for i in range(d, len(mylist)):
            while (i >= d and mylist[i]<mylist[i-d]):
                mylist[i],mylist[i-d] = mylist[i-d],mylist[i]
                i -= d
        d = d//2 if d%2 == 0 else d//2+1
    return mylist

if __name__ == "__main__":
    mylist = [18, 23, 56, 78, 70, 45, 36, 72, 34]
    print(shellSort(mylist))