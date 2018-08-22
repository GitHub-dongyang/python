#-*- coding:utf-8 -*-
#石头剪刀布
import random

'''
#1. 输出提示信息并且获取需要用户输入的信息
input("请输入你要出什么拳——石头-（1）,剪刀（2）,布-（3）——:")I
#2. 对用户所输入的值进行判断
'''
player_Value = int(input("石头1,剪刀2,布3："))
computer_Value = random.randint(1,3)

if (player_Value== 3 and computer_Value== 1)  or (player_Value== 2 and computer_Value== 3) or (player_Value== 1 and computer_Value== 2):
	print("恭喜你，你赢了！")
elif computer_Value == player_Value:
	print("平手")

else:
	print("不好意思，你输了！")
