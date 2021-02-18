"""
#1.判断 代码块 缩进
#三种表示：if;   if...else...;   if...elif...else
# a = int(input("请输入a的值:"))
# if a == 1
#     print("a=1时运行")
###### == 判断是否相等
###### = 赋值
# if a > 10 and a <=20:
#     print("a比b大")
# elif a > 20 and a != 55:
#     print("a=b时运行")
# elif a == 55:
#     print("-----a等于55")
# else:
#     print("a小于b")

######exit()方法-----退出
######in表示在...里面
# a = int(input("请输入："))
a = input("请输入：")
print(type(a))
if a == "":
    print("a不能为空")
    exit()
if a in "169890225578945": #in表示在...里面
    a = int(a)
    if a > 5:
        print("a>5时输出")
    else:
        print("a不在列表内")
        exit()  #退出

######is后面接数据类型(int,str,bool,dict,list,tuple,float)
a = 10
if type(a) is int:
    print("是数字")
elif type(a) is str:
    print("是字符串")
else:
    print("其他")
"""

#2.循环(for,while)

#while循环
# a = 1
# while a < 9:
#     print(a,"a<9")
#     a = a + 5

"""
#练习：现在十个学生的成绩，需要录入到系统中。(用while循环实现)
#十个人的姓名分别是：棉花糖、冰激凌、哆啦A梦、气球、杨慕、金晶、周大、琉璃、末末、顾默
#十个人的姓名需与其成绩一一对应
#大于60的和小于60的需要分开存放
name = ["棉花糖","冰激凌","哆啦A梦","气球","杨慕","金晶","周大","琉璃","末末","顾默"]
highmark = {} #定义一个空字典，存储大于60的信息
lowmake = {} #定义一个空字典，存储小于60的信息
a = 0 #定义一个变量，用来控制数组的下标的变化
while a < len(name): #所有信息录入都用input，故用循环--len判断数组
    grade = input("请输入"+name[a]+"的成绩：") #录入信息(+号拼接)
    if grade =="":
        print("成绩不能为空！")
    elif type(grade) is str:
        grade = int(grade) #为方便判断，转换为int格式
        if grade >60:
            highmark[name[a]] = grade  #存到字典中
        else:
            lowmake[name[a]] = grade
        a = a + 1  #控制下标变化
    else:
        print("请输入正确的值！")
        exit()
  
print("大于60的成员集合",highmark)
print("小于60的成员集合",lowmake)
"""

#for 循环，遍历

# a = [1,4,7,8.9,"m",6] #a可以是字符串、列表等
# for i in a: #i是遍历a对象的所有值
#     print(i)
######range()函数--左闭右开原则--range(开始数,结尾数(-1),步长)

# b = list(range(0,10)) #自动生成一个数列，步长默认为1
# print(b)
# for i in range(9):
#     print(i)
# b = list(range(0,10,3))#步长为3
# print(b)

"""
#练习：现在十个学生的成绩，需要录入到系统中。(用for循环实现)
#十个人的姓名分别是：棉花糖、冰激凌、哆啦A梦、气球、杨慕、金晶、周大、琉璃、末末、顾默
#十个人的姓名需与其成绩一一对应
#大于60的和小于60的需要分开存放

name = ["棉花糖","冰激凌","哆啦A梦","气球","杨慕","金晶","周大","琉璃","末末","顾默"]
highmark = {} #定义一个空字典，存储大于60的信息
lowmake = {} #定义一个空字典，存储小于60的信息

# for i in range(0,len(name)):
#     grade = int(input("请输入"+name[i]+"的成绩:"))
#     if grade >= 60:
#         highmark[name[i]]=grade
#     else:
#         lowmake[name[i]]=grade
    
# print("大于60的成员集合",highmark)
# print("小于60的成员集合",lowmake)
#for循环或替换为：
for i in name: 
    grade = int(input("请输入"+i+"的成绩:"))
    if grade >= 60:
        highmark[i]=grade
    else:
        lowmake[i]=grade
print("大于60的成员集合",highmark)
print("小于60的成员集合",lowmake)
"""
"""
#练习：打印九九乘法表
for a in range(1,10):
    for b in range(1,a+1):
        c = a * b
        print(b,"*",a,"=",c,end="  ")#写了end就不会换行,end后的""输入的字符会被打印出来
    print()
"""

"""
#练习1：通过print打印，模拟一个红绿灯的功能，注意：红灯40次，绿灯35次，黄灯3次
a = 1
while a < 10:
    for red in range(40,-1,-1):
        print("红灯还有",red,"秒变成绿灯")
    for green in range(35,-1,-1):
        print("绿灯还有",green,"秒变成黄灯")
    for yellow in range(3,-1,-1):
        print("黄灯还有",yellow,"秒变成红灯")

#######第二种方法
# while True: 
# light = {"red":40,"green":35,"yellow":3}
# for a in light:
#     for b in range(light[a]):
#         print(a,"light还有",light[a]-b,"秒")
"""






#练习2：使用代码，实现一个注册功能。用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头，存储到字典中，{username:password}

personinfo = {}
a = 1
while a < 9:
    username = input("请输入账号：")
    if username == "":
        print("账号不能为空！") 
    elif len(username)>=5 and len(username)<=8:
        if username[0] in "abcdefghijklmnopqrstuvwxyz":
            password = input("请输入密码：")
            if password == "":
                print("密码不能为空！")
            elif len(password)>=5 and len(password)<=12:
                personinfo[username]=password
                print("注册成功！账号密码为：",personinfo)
                exit()
            else:
                print("密码格式输入不正确！")
        else:
            print("账号必须小写开头")
    else:
        print("账号格式输入不正确！")
    






