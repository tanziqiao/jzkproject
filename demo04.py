"""
#1.break跳出循环和终止循环(仅跳出一层循环)
#continue和break
for i in range(10):
    if i == 4:
        continue  #跳过该条件继续循环
    if i == 7:
        break  #跳出循环
    print(i)
"""

#2.函数(方法)
#格式：
# def方法的声明 + 方法的名字自定义(方法的参数--可有可无) + 方法的说明 + 方法的逻辑代码 + return
# return 返回值，返回后我们可以对这个值做其他的操作
# """
# a = [1,2,1,1,2,3,1]
# x = a.index(2)
# print(x)
# print(a[x])
# """
# def jiafa(a,b):
#     """这个方法的作用是实现两个数字相加"""
#     if type(a) is int and type(b) is int:
#         print(a+b)
#     else:
#         return "输入的数据类型不正确"
# jiafa(1,2)


#3.异常捕获：try...except...
# def jiafa(a,b):
#     """这个方法的作用是实现两个数字相加"""
#     if type(a) is int and type(b) is int:
#         print(a+b)
#     else:
#         return "输入的数据类型不正确"
# ###############
# try:
#     jiafa(1,5)
# except Exception as e:  #异常类
#     print("上面的代码写错了",e)

#包 ——模块 —— 类 —— 方法 —— 变量
#并列
#异常类：try...except...


#4.python的包
############python自带的包
# import time #导入时间的包
# import random #导入随机的包
# for a in range(9):
#     time.sleep(1) #time包中的.sleep表示停顿多少秒
#     print(a)
# b = random.randint(100,1000) #.randint内输入范围,在范围内随机生成一个数据
# print(b)

##########python安装第三方的包
# 使用pip安装
# pip install 包名  （安装第三方包）
# pip uninstall 包名  （卸载第三方包）
# pip list /pip3 list 列出查看已安装的包
# 常用的第三方包：
# pymysql(操作mysql数据库)、selenium(web自动化)、appium(app自动化)、
# requests(接口自动化)、xlrd(操作excel表)、xlwt(写入excel表)...


#练习：定义一个方法，用来判断用户输入的账号密码是否符合规范
def personinfo():
    while True:
        username = input("请输入账号：")
        if username == "":
            print("账号不能为空！") 
        elif len(username)>=5 and len(username)<=8:
            if username[0] in "abcdefghijklmnopqrstuvwxyz":
                password = input("请输入密码：")
                if password == "":
                    print("密码不能为空！")
                elif len(password)>=5 and len(password)<=12:
                    print("注册成功！账号密码为：",{username:password})
                    exit()
                else:
                    print("密码格式输入不正确！")
            else:
                print("账号必须小写开头")
        else:
            print("账号格式输入不正确！")

personinfo()























