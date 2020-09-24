# -*- coding:utf-8 -*-
# Author:Candlia
'''
插入排序：将待排序的记录按照关键字大小的值插入到已排序的序列中的正确位置，依次重复；
直到全部记录都插入完成。其主要步骤如下：
1》将list[i]存放在临时变量p中
2》将P与list[i-1],list[i-2]......list[0]比较，若有p<list[j].key(j=i-1,i-2...0),
则将list[j]后移一个位置，直到p>=list[j].key为止。当p>=list[j].key时将p插入到list[j+1]
的位置
3》令i=1、2、3、...、n-1，重复步骤1,2,3.
时间复杂度：O（n*n)
空间复杂度：O（1）
'''
def insertSort(mylist):
    for i in range(1, len(mylist)):
        p = mylist[i]
        j = i-1
        while j >= 0:
            if mylist[j] > p:
                mylist[j+1] = mylist[j]
                j -= 1
            else:
                break
        mylist[j+1] = p

if __name__ == "__main__":
    testlist = [2,4,5,45,36,72,34]
    insertSort(testlist)
    print(testlist)