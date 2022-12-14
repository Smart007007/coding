





#函数:是组织好的，可重复使用的，用来单一或关联功能的代码段
#函数特性:提高应用模块的特性和代码的重复利用性
#函数如何定义
"""
函数名命名规则:使用字母数字下划线组成，不能以数字开头，不能使用关键字命名，不能使用已存在的函数或模块进行命名
def 函数名():任何传入的参数和自变量必须放入括号内;冒号是函数的起始，换行后缩进
    pass    pass代表占位符
    "执行语句块"
    :return     return表达式结束函数，把函数中具体的结果运行结果返回给调用方，如果不带表达式return相当于返回none（空）
"""
# def jiafa(a,b):
#     return a+b
# def jianfa(a,b):
#     print("减法结果为：",a-b)
# a=1
# b=2
# result=jiafa(a,b)
# print(result)
# print("-------------")
# result1=jianfa(a,b)
# print(result1)
# print("-------------")
# 函数类型
# """
# 有参数有返回值
# 有参数无返回值
# 无参数有返回值
# 无参数无返回值
# """
# def sub(a=1,b=8):
#     return a*b
# print(sub())
#
# def div():
#     x=10
#     y=2
#     print(x/y)
# div()

#2、关键字参数:通过实参名指定给某个形参，形参或实参的位置可以变；PS：如果里面有位置参数，先写位置参数，在写关键字参数
# def jia1(a,b,c):
#     print("a的值是：",a)
#     print("b的值是：",b)
#     print("c的值是：",c)
# jia1(a=4,b=2,c=3)
#
# #3、默认参数:调用参数时没有实参(不传参)，使用函数中自定义;PS:如果有入参，优先使用实参值
# def jia2(a=1,b=5,c=8):
#     print("a的值是：", a)
#     print("b的值是：",b)
#     print("c的值是：",c)
#
# jia2(10,20)
#
# # 4、不定长参数:调用函数时可以传入0个或多个实参
# #*args：接收多传入的位置参数，以元组的形式保存，*解析元组数据
# def jia3(*args):
#     print(*args)
#
# jia3(10,20,30)
#
# #5、特殊参数:在关键字参数的第一个形参前放置一个*
# def jia4(a=1,*,b=5,c=8):
#     print("a的值是：", a)
#     print("b的值是：",b)
#     print("c的值是：",c)
#
# jia4(10,b=20,c=30)

# #匿名函数:关键字lambda
# def sum1(x=100,y=101):
#     return x+y
# print(sum1())
#
# sum2=lambda x,y,z:x+y+z
# print(sum2(2,3,4,))
#



































