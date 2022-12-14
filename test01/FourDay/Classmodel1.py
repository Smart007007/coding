# -*- encoding：utf-8 -*-
# @Time:2022/10/31 15:55
# @Auto:guohuashang
# @FileName:classModel1.py
# @Emial:
# @Function:
class Student:
    name="你猜"
    def __init__(self,sex,name):
        self.sex=sex
        self.name=name
    #类方法，必须跟随self
    def say_self_name(self):
        print(self.name)
    #实例方法, 方法后跟随cls,
    @classmethod
    def say_cls_name(cls):
        print(cls.name)
    #静态方法,方法名后不用跟随self
    @staticmethod
    def say_static_name():
        print("谁的名字？")

#类的实例化
# huashang=Student("boy","huashang")
# # huashang.say_self_name()
# # huashang.say_cls_name()
# huashang.say_static_name()






