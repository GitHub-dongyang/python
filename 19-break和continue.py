#break和contiue

i= 1
while i<= 10:
	print(i)
	i+= 1
	if i== 3:
#break:是在满足break的条件后，结束整个while循环，然后开始下一个代码
#continue：是在满足continue的条件后，结束当前这一次循环continue之后的代码，不再执行continue之后的代码，返回到while循环，重新开始循环！
		continue
		#break
	print("=========")
print("换行")
