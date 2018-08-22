#-*- coding:utf-8 -*-

sex = input("请输入您的性别--:")#输入男或者女
if sex== ("男"):
	print("hello,boy!")
	height = int(input("你身高多少呢--："))#输入数字，单位cm
	money = int(input("你有多少钱呢--："))#输入数字，单位￥
	beautiful = input("你帅吗--：")#输入帅或者不帅
	if height>= 170 and money>=100000 and  beautiful == ("帅"):
		print("哇，帅哥你是高富帅啊！我们做朋友吧！")
	else:
		print("唉！哥们你还是再努力吧！你不是我要的菜！")

elif sex== ("女"):
	print("hello,girl!")
	height = int(input("你身高多少呢--："))#输入数字，单位cm
	money = int(input("你有多少钱呢--："))#输入数字，单位￥
	beautiful = input("你美吗--：")#输入美或者不美
	if height>= 165 and money>=100000 and  beautiful == ("美"):
		print("哇，美女你是白富美啊！我们做朋友吧！")
	else:
		print("唉！美女你还是再努力吧！你不是我要的菜！")
else:
	print("我去，你是泰国的吧！想吐……")
