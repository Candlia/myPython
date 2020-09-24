# -*- coding:utf-8 -*-
# Author:Candlia
'''
大顶堆：每个节点的值都不小于其孩子节点
小顶堆：每个节点的值都不大于其孩子节点
堆排序：利用完全二叉树特性的一种选择排序，当堆顶元素和堆中的最后一个元素交换位置后，
根节点和其子节点的关键字值不再满足堆的定义，需要进行调整。
用筛选法调整堆是将根节点与左右孩子节点的关键字值比较，其与较小关键字值的孩子节点进行交换。
被交换的孩子节点所在的字树可能不再满足堆的定义，重复对不满足定义的子树进行操作，直到堆建成。
调整堆的主要步骤;
1》设置变量i为需要调整的序列的最小下标low，设置变量j=2i+1,设置变量P=list[i]
2》当j<high-1时，若list[j]>list[j+1],j+1
3》若p>list[j],则list[i]=list[j],i=j,j=2i+1
4》重复步骤2,3，直到j>=high
5》list[i]=p
时间复杂度：O(nlogn)
'''

def sift(arr,low,high): #调整为小顶堆
    i = low            #low为父节点
    j = 2*i + 1        #j为对应的孩子节点
    p = arr[i]         #父节点的值
    while j < high:     #high为最大孩子节点下标
        if j < high-1 and arr[j] > arr[j+1]:  #比较左右孩子大小
            j += 1                  #j为当前节点最小孩子下标
        if p > arr[j]:              #不满足小顶堆，调整
            arr[i] = arr[j]
            i = j
            j = 2*i+1
        else:
            j = high + 1
        arr[i] = p
def heapSort(arr): #小顶堆输出为倒叙
    lenth = len(arr)
    for i in range(lenth//2-1, -1, -1):
        sift(arr, i, lenth)
    print(arr)
    for i in range(lenth-1,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        sift(arr,0,i-1)
    return arr


if __name__ == "__main__":
    test = [100,70,50,20,90,75,60,25,10,85,65,80]
    print(heapSort(test))