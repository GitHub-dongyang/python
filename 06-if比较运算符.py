#if比较运算符
'''
两者在一起的时候，中间不能有空格！
大于等于 >=
小于等于 <=
等于 ==
赋值 =
不等于 !=python3中表示不等于的方式
       <>python2中可以用这种方式表示不等于，但是python3中不可以
'''
#if逻辑运算符
#或者：or
#并且：and
#取相反值：not


#逻辑运算符 and & or
you = input ("你去吗？")
youWife = input ("你老婆去吗？")
if you == "去" and youWife == "去":
	print("ok!")
else:
	print("no!")


#逻辑运算符 not
a = int(input("请输入你的值--："))
if not a>0 and a<=50:
	print("你所输入的值不在0——50之间，是正确的！")
else:
	print("你所输入的值在0——50之间，是错误的！")
