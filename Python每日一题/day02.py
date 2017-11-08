#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/8 下午11:54
# @Author  : Hanni
# @Fun     : 设计一个猜数字的游戏，系统随机生成一个1~100之间的整数，玩家有5次机会，
#            每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，则告知玩家并提前结束游戏，
#            如果5次都没猜中，结束游戏并告知正确答案。

'''
用面向对象的编程方式来实现，既然是面向对象，我们就要换一个角度来把问题抽象化，
这个游戏有4个属性，分别是随机数的取值范围，min和max，目标值 target，猜测次数 choice，
另有还有一个方法用于如何猜游戏，随着需求的变化，我们可以不断地加其他属性和方法。
'''

import random

class GuessGame:
    def __init__(self, min_num, max_num, choice):
        """
        :param min_num: 最小值
        :param max_num: 最大值
        :param choice: 中奖机会
        """

        self.max_num = max_num
        self.min_num = min_num
        self.target = random.randint(min_num, max_num)
        self.choice = choice

    def guess(self):
        """
        猜数字
        """
        choice = self.choice

        while choice > 0:
            choice -= 1
            try:
                num = int(input("输入幸运数字："))
            except ValueError as e:
                print("请输入有效数字")
                continue

            if num == self.target:
                print("恭喜你猜中了")
                break
            elif num <= self.target:
                print("你猜的数字太小了，还剩 %d 次机会" % choice)
            else:
                print("你猜的数字太大，还剩 %d 次机会" % choice)
        else:
            print("很遗憾，%d 次机会都用完了,只差一点点就猜中了，正确答案是 %d" % (self.choice, self.target))


if __name__ == '__main__':
    game = GuessGame(1, 100, 5)
    game.guess()
