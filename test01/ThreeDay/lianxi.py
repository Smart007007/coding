"""
分支结构---三种表达形式
if 条件：
       执行语句
else 条件：
       执行语句二

if 条件：
       执行语句一
elif 条件：
       执行语句二
else：
       执行语句三
"""
# age=17
# if age<=18:
#     print("未成年不允许上网")
#
# time=21
# if time>=20:
#     print("使用深夜套餐")
# else:
#     print("不能使用深夜套餐")

# if datatime=="情人节":
#     print("买玫瑰")
#     print("看电影")
#     print("开酒店")
# elif datetime=="中秋节":
#     print("买月饼")
#     print("吃团圆饭")
# elif datetime=="中元节":
#     print("祭祀")
#
# else:
#     print("每天都是节日")

#循环结构for...in...(定次循环)\while（不定次循环）----break语句和continue语句
#for...in..循环：要明确循环执行的次数或者一个容器进行迭代
#range()函数：可以用来产生一个不变的数值序列
# li=[1,2,3,4]
# for i in li:
#     if i==3:
#         continue
#     print(i)
#1、计算1-100求和
# result=0
# for i in range(1,101):
#     print(i)
#     result=result+i
# print(result)
# #2、计算1-100的奇数求和
# result=0
# for i in range(1,101,2):
#     print(i)
#     result=result+i
# print(result)
#
# #3、计算1-100的偶数求和,不实用步长，使用分支结构
# result=0
# for i in range(1,101):
#     if i%2==0:
#         print(i)
#         result=result+i
# print(result)
#
# #while循环:构造不知道循环具体次数，通过while循环通过一个能产生或转换成布尔(bool)值的表达式来控制循环
# #表达式的为True循环继续，表达式值为Flase循环结束
# i=5
# a=int(input("请输入一个数: "))
# while a>=5:
#     print("输入数对的")
# result=0
# while result<=10:
#     print(result,"小于10")
#     result=result+1
# else:
#     print(result,"大于10")

# result=0
# while result<=10:result=result+1
# else:
#     print(result,"大于10")

#break和continue语句
"""
break语句可以跳出for和whlie循环体，如果你从for或whlie的循环体中终止任何对应的循环else语句看都不会执行
continue语句跳过当前循环块中的剩下语句，继续执行进行下一轮循环
"""
#摇骰子-猜数字(6个骰子【1-36】)
#作业要求
"""
你输入的数小于骰子数，提示"你猜错了",请输入大一点的数
你输入的数大于骰子数，提示"你猜错了",请输入小一点的数
你输入的数等于骰子数，提示"恭喜你，蒙对了"！
猜错了一直继续下去，猜对了程序结束
"""
#随机函数
import random
j=random.randint(1,36)
print(j)
while True:
    s=int(input("请猜一个数:"))
    if s>j:
        print("你猜错了，请输入小一点的数！")
    elif s<j:
        print("你猜错了，请输入大一点的数！")
    elif s==j:
        print("恭喜你猜对了！")
        break













































