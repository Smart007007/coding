#类的继承
#定义父亲类
class father():
    def dabieye(self):
        print("大别野")

    def shangshigongshi(self):
        print("上市公司")
    def yiwanzichan(self):
        print("亿万资产")
    def __secretary(self):
        print("秘书")
    def yuangong(self):
        print("员工")
#定义母亲类
class mather():
    def shuangyanpi(self):
        print("双眼皮")
    def dachangtui(self):
        print("大长腿")
#定义子女类,继承可以想用继承父类大方法，也可以覆盖父类大方法；可以多继承，隐藏属性或方法
class children(father):
    print(father().shangshigongshi())
#     def yuangong(self):
#         print(1)
# print(children().yuangong())
    def yuangong(self):
        print("员工1")
children().yuangong()
