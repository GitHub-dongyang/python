#打印一个乘法口诀表

'''
\t  ==  写代码的时候tab键的作用，
\n  ==  换行


'''
#y == i,x == j,z == x*y == i*j
i = 1
while i <= 9:
	j = 1
	while j <= i:
		print("%d*%d=%d\t"%(j,i,i*j),end="")
		j += 1
	print("")
	i += 1
