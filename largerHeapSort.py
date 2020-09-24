# -*- coding:utf-8 -*-
# Author:Candlia
def heapAjust(myarr,parent):
    p = myarr[parent]
    child = 2*parent + 1
    while child < len(myarr):
        if myarr[child]<myarr[child]+1:
            child += 1
        if p<myarr[child]:
            myarr[parent], myarr[child] = myarr[child], myarr[parent]
            parent = child
            child = 2 * parent +1
        else:
            parent = parent+1
    myarr[child] = p
