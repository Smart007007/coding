#数据类型datatype
"""
1、字符串
2、数值型 (int:整形，float：浮点型)
3、布尔型: True、Flose
4、列表 (list)
5、元组 (tuple)
6、字典 (dict)
7、集合 (set)
"""
#字符串，字符串的定义，使用单引号、双引号、三引号表达
# str1='我是一个字符串'
# str2="1代表str类型"
# str3='字符串3'''
# print(type(str1),type(str2),type(str3))
#一、字符串拼接,和+
# a="a123"
# b="123x"
# c="098"
#二、字符串指定开头和结尾(startswith函数指定开头，endswith函数指定结尾)
# print(a.startswith("a"))
# print(b.startswith("a"))
# print(a.endswith("x"))
# print(b.endswith("x"))
#三、字符串转换大小写字母
randomStr="abcD"
print(randomStr.upper())#upper函数把字符串中的字母统一转化成大写
print(randomStr.lower())#lower函数把字符串中的字母统一转化成小写

# lizhe02="0123456789abcdefghijklmn"
# 四、#字符串长度使用len函数
# print(len(lizhe02))
#五、定义unicode字符串，防止中文乱码，在字符串前加小写字母u,python3不存在该问题，python2存在中文乱码
# my=u"我"
# print(my)

#六、统计字符串中某个字符出现的频率使用count函数，表达形式：字符串.count("单个字符")
# a="11bacad7891"
# print(a.count("a"))

#七、replace函数替换字符串中某个字符,例如：a="11bacad7891"；
#replace表达式：a.replace(想要替换的字符, 新的字符,替换个数)，替换个数如果不加，默认全部替换
# print(a.replace("1", "e",2))

#八、字符串格式化输出，使用%占位
#九、find函数从字符串左边开始查找字符，刀刀后返回字符串位置，找不到字符返回-1
a="11bacad7891"
print(a.find("7"))

#十、判定字符串中包含字母
"""
isalpha判断字符串由纯字母组成
isdigit判断字符串由纯数字组成
"""
# a='qa12ab'
# b='123456'
# c='abcdef'
# print(c.isdigit())
# print(a.isalnum())
# print(a.isalpha())
# print(b.isalpha())
# print(c.isalpha())

#十一、返回字符串中最大字母使用max，返回字符串中最小字母使用min
# a="ABCD"
# print(max(a))
# print(min(a))

#十二、删除字符串末尾空格
# a="1234ab    "
# print(a.rsplit())

#十三、字符串切片(前闭后开)
"""
a="1234567890"
示例：切字符串单一字符a[索引值]
全部字符：a[::],第一个冒号代表其实位置，第二个冒号代表结束位置，默认步长（跨越几个索引）为1
字符串中间取值：a[起始索引：结束索引：步长]
"""
a="1234567890"
print(a[-1])
print(a[3:7:1])

#变量,变量名相同时,最后面的值会覆盖前面的值
# c=1
# c=2
# print(f"c的值为:{c}")
#同时对多变量赋值
e,d=10,20
print(f"e的值为{e}",f"d的值为{d}")
print("-----------------------")
e,d=d,e#变量之间值互换
print(f"e的值为{e}",f"d的值为{d}")

#列表
#一、定义列表
a=[]#定义空列表
print(a)
print("-------")
b=list()#定义空列表
c=[1,2,3]#定义列表
print(type(a))
print(type(b))
print(type(c))
#二、append列表末尾增加元素
a.append("a")
c.append("a")
print(a)
print(c)
#三、insert函数按照索引位置进行添加元素，insert(索引位置，插入的元素)
c.insert(0,"b")
print(c)

#四、pop移除列表最后一位元素,不添加索引默认删除最后一位，指定索引删除索引元素
# a=[1,2,3,4,5,int,float,(1,2),"A"]
# print(a.pop(5))
# print(a)

#五、remove函数删除指定的元素，示例：remove(元素值)
# a.remove((1,2))
# print(a)
#六、sort函数列表排序，reverse=False或为空，升序；reverse=True倒叙
# li=[9,5,3,7,4,2,6,1]
# li.sort(reverse=False)
# print(li)
# 七、reverse列表倒置
# li.reverse()
# print(li)

#八、index查找其中某个元素的位置
# li=[9,5,3,7,4,2,6,1]
# print(li.index(7))

#九列表拼接
# li=[1,2]
# li1=[3,4]
# li4=("a","a1")
# li.extend(li4)#extend可迭代的对象都可以添加
# print(li)
# print("-------------")
# li2=li+li1
# print(li2)

#十、遍历列表
# li=["朋友1","朋友2","朋友3","朋友4","朋友5"]
# for i in li:
#     print(i)
#十一、set把list转成集合（集合由去重特性），去重后在转成list
li=[1,2,1,2,3]
print(set(li))
print(list(set(li)))

#元组
#一、定义元组
a=()
b=tuple()
c=(1,2)
d=(1,2)
print(type(a))
print(type(b))
print(type(c))
import operator
#eq，两元组对比，相同返回True,不同返回Flase
print(operator.eq(c, d))
#list和tuple的 区别？
#列表可改变，元组不可修改（列表可逆，元组不可逆）


#一、定义字典
dict1={}
dict2=dict()
dict3={"key":"value","name":"zhangsan"}
dict4=dict(name="zhangsanfeng")
print(dict4)

#二、添加元素
dict1["lizhe"]="02"
print(dict1)
dict1.update(b=1)
print(dict1)

#字典取值，通过key取value
# print(dict1['lizhe'])
# print(dict1.get("C"))#get方法，如果字典中没有对于的key,则返回None
# #取字典的key
# print(dict1.keys())

#取字典中所有的value
# print(dict1.values())
#
# #取字典的键值对
# print(dict1.items())

#判断某个key在不在字典中
# print("lizhe" in dict1)
# print("c" in dict1)

# 字典删除某个key
# dict1.pop("b")
# print(dict1)

#集合,特性（去重）
b=set()
c={1,23,3}
a={1,3,2}

print(type(a))
print(type(b))
print(type(c))

#集合交集
print(c.intersection(a))

#集合并集
print(c.union(a))

#差集
print(c.difference(a))
print(a.difference(c))