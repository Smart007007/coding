# 预习python数据类型
# 预习运算符
# 作业，输出小名片，表达形式
"""
姓名：张三
年龄：18
手机号：13812345678
Email：13812345678@163.com
Address:河南省郑州市金水区农业路18号
"""
"""
要求：
1、使用变量
2、使用输入函数
3、至少4中方法实现
"""
# -*- encoding：utf-8 -*-
#keyword=input("请输入你想展示的内容:")
#print (keyword)

#input("提示语：")
name='张三'
Age=18
MobileNumber=13812345678
Email='13812345678@163.com'
Address='河南省郑州市金水区农业路18号'

# name=input("姓名:")
# Age=input("年龄:")
# MobileNumber=input("电话号:")
# Email=input("邮箱:")
# Address=input("地址:")

print(f"名字:{name}"+f" 年龄:{Age}"+f" 电话号:{MobileNumber}"+f" 邮箱:{Email}"+f" 地址:{Address}")
print("名片信息:{}".format(name),format(Age),format(MobileNumber),format(Email),format(Address))

print("名字%s"%name,"年龄%s"%Age,"电话号%s"%MobileNumber,"邮箱%s"%Email,"地址%s"%Address)
print('名字'+name+"年龄"+'Age'+"电话"+'MobileNumber'+"邮箱"+Email+"地址"+Address)






















































