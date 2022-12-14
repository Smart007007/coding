"""
单元测试框架: unitest(python内置)、pytest(三方库)--基于unittest进行二次开发
unittest四大组件:测试脚手架test fixture、测试用例TestCase、测试套件test suite、测试运行器（test runner）
搭建自动化测试框架、python的白盒测试--单元测试框架的思维逻辑
断言:软件运行的实际结果与预期结果的对比，产生一个新的结果(三种状态:Pass、Fail、Error  PS:跳过的用例标记为成功状态)
unittest中测试用力执行顺序:遵循ASCII码(A-Z、a-z、0-9)、从test后一位开始对比长度不一致补位为0
setUp/tearDown方法: 继承TestCase中的方法，运行规则(每条测试用例之前先运行一次setUp方法，再运行)
setUpClass/tearDownClass实例方法:运行规则(无论有多少条用例，都只执行一次，setUpClass在所有方法前执行，tearDownClass在所有方法后执行)
"""
# #导入unittest
# import unittest
# #定义测试用例类，并继承tset
# class TestDemo(unittest.TestCase):
#     #定义测试用例方法
#     def test_0001(self):
#         pass
#     def test_0002(self):
#         pass
#     def test_0019(self):
#         pass
# if __name__== '__main__':
#     unittest.main()

# import unittest
# class TestDemo(unittest.TestCase):
#     def test_ASDFG(self):
#         pass
#     def test_aaSSDF(self):
#         pass
#     def test_Hkghhij456(self):
#         pass
# if __name__ == '__main__':
#         unittest.main()
import unittest
class TestDemo(unittest.TestCase):
    def test_u2345(self):
        self.assertEqual(1,2)
    def test_uyeri(self):
        self.assertNotEqual(1,2)
    def test_87273(self):
        pass
if __name__=='__main__':
    unittest.main()
