python右两种注释：

1：单行注释
	#给下一行内容添加注释（类似当前注释）
	print("hello world!")
	print("hello world!") #给当前行添加注释（类似当前注释）
2：多行注释
    用成对的 单引号 或者 双引号
	"""
	print("hello world")
	print("hello world")
	print("hello world")
	print("hello world")
	print("hello world")
	print("hello world")
	"""

	'''
	print("hello world")
	print("hello world")
	print("hello world")
	print("hello world")
	print("hello world")
	print("hello world")
	'''
#python解析器目前分为2和3版本，
python2     在.py文件中不能有中文，如果有中文则报错
而python3   在.py文件中可以有中文
如果想要用python2解析器，运行包含中文的.py文件，需要在首行添加 
 （#coding=utf-8） 或者 （#-*- coding:utf-8 -*-） 
