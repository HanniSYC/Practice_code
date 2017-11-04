#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/3 下午9:38
# @Author  : Hanni
# @Fun     : 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
#            请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

print '欢迎来到二维数组中的查找v1.0 @星辰\n'

class Solution:

    def Find(self, target, array):
        rowcount = len(array)
        colcount = len(array[0])
        if colcount - 1 == 0: #二维数组为空
            return False

        for i in range(rowcount -1 , -1, -1):#从左下角开始检索,到右上角结束，每次移动一个位置

            if target > array[i][0]:#要查找的数字大于左下角的数字
                for j in range(colcount):#右移比较
                    if target == array[i][j]:#找到，返回True
                        return True

            elif target == array[i][0]:#要查找的数字等于左下角的数字，返回True
                return True
            #否则上移
        return False


array = [[1,3,5,7],[2,4,6,8],[3,6,9,12]]

#循环显示二维数组
for i in range(0, 3):
    for j in range(0, 4):
        print array[i][j],
    print

target = input('请输入待检测的数字：')

s = Solution()
print(s.Find(target, array))
