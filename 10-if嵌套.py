#-*- coding:utf-8 -*-

danger = input("检测是否有危险物品：")#有或者没有
if danger == ("没有"):
	print("进入候车大厅，等待检票！")
	ticket = input("检测是否购买正规车票：")#有或者没有
	if ticket == ("有"):
		print("候车台，等待上车！")
	else:
		print("买票去，没有票不能上车")
else:
	print("不可以进入候车大厅，等待公安吧！")
