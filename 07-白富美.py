#-*- coding:utf-8 -*-

color = input("你白吗？--类似白或者不白：")   #白或者不白
rich = int(input("你有多少钱？--类似1000："))  #输入有多少钱
beautiful = input("你漂亮吗？--类似yes或者no：")#输入yes或者no
if color == "白" or rich >= 10000 and beautiful == "yes":
	print ("这样的女人可以娶了！")
else:
	print("你还是算了吧！")
