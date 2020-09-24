# -*- coding:utf-8 -*-
# Author:Candlia
'''
冒泡排序是两两比较待排序记录的关键字，如果次序相反则交换两个记录的位置，
直到序列中所有记录有序。若按升序排序，每趟将最大元素交换到最后的位置，就像气泡从水中冒出。
主要步骤：
1》设交换次数k=1
2》在常数为n的序列{a[0],a[1],...,a[n-1]}中从头到尾比较a[i]和a[i+1],若a[i]>a[i+1],
则交换两个元素的位置，其中，0<=i<n-i
3》k增加1
4》重复步骤2,3，直到步骤2中未发生交换或者k=n-1
'''

def bubbleSort(arr): #按照降序排序
    k = 0
    sortTime = 1
    flag = True
    while sortTime < len(arr) and flag:
        flag = False
        for i in range(len(arr)-1):
            if arr[i+1] > arr[i]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
                k += 1
                flag = True
        sortTime += 1

    return arr


if __name__ == "__main__":
    mylist = [2,23,18,56,78,70,45,36,72,34]
    print(bubbleSort(mylist))