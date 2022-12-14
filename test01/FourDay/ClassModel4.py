#倒入类（来自于包.模块 导入类）
# from fourthDay.classmodel2 import student
# class classDemo(object):
#     student().say_you_Info("张三",20,"开车")
# from fourthDay.classModel1 import Student
# class classDemo1():
#     print(Student().a)
#导入模块
from fourthDay import classmodel3
class classDemo2(classmodel3.father,classmodel3.mother):
    pass
# 导入classmodel3模块下所有内容
from fourthDay.classmodel3 import *
class classDemo3(father,mother):
    pass

#引入标准库中的模块
import time,sys,datetime,json
print(sys.path)#打印当前文件位置
#打印时间戳

print(time.time())
print(datetime.datetime.now())#打印当前时间
a={"a":1,'b':2}
print(type(a))
b=json.dumps(a)#dumps把字典转成json字符串
print(type(b))
c=json.loads(b)#loads把json字符串转为字典
print(type(c))

"""
作业：
1、把周末作业转换成类的方式实现
2、预习yaml、Excel、xml、txt文件的读取
3、预习unittest\pytest
"""






