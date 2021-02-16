"""
#1.python中的数据类型
print("字符串","hello world!")  #字符串str
print("整数",2333)  #整数int
print("小数",2.333)  #小数float
print("布尔值",True,"和",False)  #布尔值bool
print("元祖符号",())  #元祖tuple
print("列表符号",[])  #列表list
print("字典符号",{})  #字典dict
# 单行注释
"""



"""
#2.变量和赋值(学习input输入)
# a = "小布"   #赋值给a变量，变量必须是小写字母，不能有特殊符号
# print(a)
#input只能输入字符串格式
############字符串格式转换规律
############1.任何数据都可以转换为字符串
############2.整数和小数可以互相转换
############3.字符串转换为其他数据格式必须满足长得像这个规律
a = int(input("请输入a的值："))
b = int(input("请输入b的值："))
print("input获取的内容：a+b=",a+b) #这里的a+b是字符串的拼接
"""



#3.python中的len()方法(获取字符串的长度，只适用于字符串、元祖、列表和字典)
# a = 'ajfnedngdfklmbier2430nbdfjkb mfd'
# print(len(a))

#练习：通过代码获取两段内容，并且计算他们的长度的和
a = input("请输入第一段内容：")
b = input("请输入第二段内容：")
print("获取a和b两段内容：",a+b,"a和b两段内容的长度之和:",len(a+b))
# print("a和b两段内容的长度之和:",len(a)+len(b))
