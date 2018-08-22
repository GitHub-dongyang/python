#while嵌套中的break和continue

i= 1
num = int(input("请输入要显示多少行："))
p_Num= '总共打印了{}行'.format(num)
while i<= num:
	j=1
	while j<= i:
		print("*",end=" ")
		print('=========')
		j+= 1

#比较while嵌套中break和continue的作用
		continue
		#break
	print("")
	i+= 1
print(p_Num)
