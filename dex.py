#Python练习题---简单的进制转换器

import base64
import time

def Decimal_conversion():
	dec = int(input ('输入需要转换的十进制数字：'))
	print ('十进制为：',dec)
	print ('二进制为：',bin(dec))
	print ('八进制为：',oct(dec))
	print ('十六进制为：',hex(dec))

def Octal_conversion():
	dec = int(input ('输入需要转换的八进制数字：'),8)
	print ('十进制为：',int(dec))
	print ('二进制为：',bin(dec))
	print ('八进制为：',oct(dec))
	print ('十六进制为：',hex(dec))	

def Binary_conversion():
	dec = int(input ('输入需要转换的二进制数字：'),2)
	print ('十进制为：',int(dec))
	print ('二进制为：',bin(dec))
	print ('八进制为：',oct(dec))
	print ('十六进制为：',hex(dec))

def Hexadecimal_conversion():
	dec = int(input ('输入需要转换的十六进制数字：'),16)
	print ('十进制为：',int(dec))
	print ('二进制为：',bin(dec))
	print ('八进制为：',oct(dec))
	print ('十六进制为：',hex(dec))	

def Base64_conversion():
	dec = str(input ('输入需要转换的字符：'))
	try :
		mid = base64.b64decode(dec.encode('utf-8'))
		print('base64解码为：',mid.decode())
	except:
		print('base64编码为：',str(base64.b64encode(dec.encode('utf-8')),'utf-8'))


def Ascii_conversion():
	dec = input('输入需要转换的字符：')
	if dec.isdigit():
		print('该Ascii码对应的字符为：',chr(int(dec)))
	else:
		print('该字符对应的Ascii码为：',ord(str(dec)))

functions = {
	1:Decimal_conversion,
	2:Octal_conversion,
	3:Binary_conversion,
	4:Hexadecimal_conversion,
	5:Base64_conversion,
	6:Ascii_conversion,
}
localtime = time.asctime(time.localtime(time.time()))
print ('''
*************进制转换************
1.十进制转换其他进制
2.八进制转换其他进制
3.二进制转换其他进制
4.十六进制转换其他进制
5.Base64编码转换
6.Ascii编码转换
	''','\n'+localtime)

choice = int(input('选择功能：'))
functions.get(choice)()
