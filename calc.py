#python练习题--简单计算器

def calc(arg1,cal,arg2):
	arg1=float(arg1)
	arg2=float(arg2)
	if cal == '+':
		print('两数相加和为：',arg1+arg2)
	elif cal == '-':
		print('两数相减和为：',arg1-arg2)
	elif cal == '*':
		print('两数相乘和为:',arg1*arg2)
	elif cal == '/':
		print('两数相除和为：',arg1/arg2)
	else:
		print('运算符错误!')

a=input('输入需要运算的算术式：')
b=['+','-','*','/']
for c in list(a):
	if ord(c) in range(32,48) or ord(c) in range(58,65):
		d=a.split(c)
		d.insert(1,c)
		break

calc(*d)