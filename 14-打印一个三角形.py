#-*- coding:utf-8 -*-

#打印一个形状，类似下面的
# *****
# *****
# *****
# *****
i= 1
while i<= 5:
	num= int(input("请输入当前行有多少个*数目--：")) 
	j= 1
	while j<= num:
		print("*",end="")
		j+= 1
	print("")
	i= i+1
