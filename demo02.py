"""
#1.元祖,下标，从0开始编号
# a = (1,2,3,4,5,6,7,8.8,"字符串","字符串",True,False,"字符串") 
# print(a[8]) #仅打印下标为8的元祖数据
# print(a[-2]) #仅打印最后一位的值

#切片(利用下标批量取值)，左闭右开
a = (1,2,3,4,5,6,7,8.8,"字符串","字符串",True,False,"字符串") 
print(a[0:8])  #取下标从0到7的值
print(a[:8])  #取下标从0(开头)到7的值
print(a[8:])  #取下标从8到结尾的值
print(a[:])  #取从开头到结尾的值

#寻找元祖的下标方法(count 和 index只能操作一维元组)
#.count -- 统计某个值的数量
#.index -- 查找某个值的下标
# print(a.index("字符串")) # 查找a元组中的数据为"字符串"的下标，多个相同字符仅显示第一次出现的位置
# print(a.count("字符串")) #统计a元组中为"字符串"的文本数据出现的次数

#二/三/...维元组
a = (1,2,3,4,5,6,7,8.8,"字符串","字符串",True,False,"字符串") 
b = (a,1,8,9,6) #b是一个二维元组
c = (b,6,8) #c是一个三维元组
print(b[0]) #取a的元组
print(b[0][2]) #取a中的下标为2的值
print(c[0]) #取b中的值和b中包含a的元组
print(b.index(1))

"""
"""
#2.列表
# a = [1,2,3,4,5,6,7,8.8,"字符串","字符串",True,False,"字符串"]
# print(a[8]) #仅打印下标为8的列表数据
# print(a[-2]) #仅打印最后一位的值

#注意：元组和列表的区别：元组一定，写好后不可修改，而列表可以修改

#对列表的值进行修改的方法
#.count -- 统计某个值的数量
#.index -- 查找某个值的下标
#.append -- 向列表中追加数据
#.insert -- 向列表中指定位置插入数据
#.pop -- 剪切数据
#.clear -- 清空列表数据
#.extend -- 合并列表,向列表中追加数据,可以追加一个列表

a.append("append1") #仅能将数据追加到最后,且仅支持追加一个参数
a.insert(3,"append1") #在a列表中下标为3的地方插入"append1"
b = a.pop(7) #将下标为7的进行剪切赋值给b
b = ["extend1","extend2"]
a.extend(b)
print(a+b)与a.extend(b)实现效果一致
.remove -- 删除某个值
a.remove(8.8) #仅能删除第一次出现的该值
"""

"""
#3.字典
#字典的特点：
#字典中的值没有顺序
#字典的接口必须是键值对的结构 -- key:value  
#如:a = {"name":"mianhuatang",0:"字符串","age":22}
a = {"name":"mianhuatang",0:"字符串","age":22}
#####取值=get
print(a["name"])
b = a.get("name")
print(b)
#####新增=updata
a["high"] = "183cm"
print(a)
b = a.update(high="183cm")
print(a)
#####剪切=pop
b = a.pop("name")
print(a)
print(b)
#####修改=updata
a["name"] = "bingqiling"
print(a)
b = a.update(name="yangmuer")
print(a)

#列表和字典的删除方法
del a["name"]
print(a)
"""

#练习：获取用户输入的个人信息，并且存储到字典中。(个人信息包括了：name,age,sex)
name = input("请输入用户name:")
age = int(input("请输入用户age:"))
sex = input("请输入用户sex:")
# userinfo = {"name":name,"age":age,"sex":sex}
userinfo = {}
# userinfo.update(name=name,age=age,sex=sex)
userinfo["name"] = name
userinfo["age"] = age
userinfo["sex"] = sex
print(userinfo)