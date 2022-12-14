# -*- encoding：utf-8 -*-
#keyword=input("请输入你想展示的内容:")
#print (keyword)
#变量:像内存申请空间,用于临时存储数据,使用完则释放内存
#变量命名方法：驼峰命名法 (大驼峰、小驼峰)
"""
#变量命名规则: 由字母开头下划线组成
#1、不能以数字开头
#2、不能包含特殊字符
#3、不能使用保留(关键字)命名
#"""

# for=input(请输入你想展示的第二个内容: ")
#print('立哲02期开启python基础学习')
#查看关键字
#import keyword
#print(keyword.kwlist)

studentName='张三'#小驼峰
SchoolName='哈哈'#大驼峰
#字符串的处理标准格式化输出f-string
print(f"学生姓名是：{studentName}"+f"他总是{SchoolName}大笑")
#字符串的处理「标准格式化输出」format
print("学生姓名是:{}".format(studentName))
#格式化输出
#s代表字符串，f代表浮点数，d代表整数，e保留小数点后6位
print("%s"%studentName)
a="1.1"
print("这个数是：%s"%a)
b=1.123456789
print(round(b))#四舍五入，不指定位数取整
print(round(b,3))#取小数点后几位，round函数最后的一个值，决定小数点长度
print(b)


#一个等号叫赋值，两个等号才是等于
#定义变量a,把1赋值给a
a=1
b=1
c=2
d=3
#输出a是否等于b,如果等于打印true,不等于打印false
print(a==b)
print(a==c)
#type函数获取数据类型
print("这是a的类型",type(a))
#id函数获取内存存储地址
print("这是a的id",id(a))
# 两字符串拼接,拼接后两字符串之间由空格
print("这是b的类型",type(b))
print("这是b的id",id(b))
print("这是c的类型",type(c))
print("这是c的id",id(c))
print("这是d的id",id(d))
















